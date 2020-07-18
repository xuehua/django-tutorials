from django.db import models
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey


# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=exclude)
        qs = self.__class__._default_manager.filter(
            state=self.state,
            name=self.name    
        )

        if self._state.adding and qs.exists():
            raise ValidationError('The city already exists.')

    def __str__(self):
        return f"{self.state.name}: {self.name}"

class Firm(models.Model):
    firm = models.CharField(max_length=50)

    def __str__(self):
        return self.firm

class FirmLocation(models.Model):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE) 
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = ChainedForeignKey(
            City,
            chained_field='state',
            chained_model_field='state',
            show_all=False,
            auto_choose=True,
            sort=True)
    # city = GroupedForeignKey(City, "state")
    street = models.CharField(max_length=50)

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=exclude)

        qs = self.__class__._default_manager.filter(
            firm=self.firm,
            city=self.city    
        )

        if self._state.adding and qs.exists():
            raise ValidationError('The firm location already exists.')

    def clean(self):
        if self.city.state != self.state:
            raise ValidationError(f"State '{self.state}' and City '{self.city}' are inconsistent")

    def __str__(self):
        return f'{self.firm}: {self.city}'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    firm_location = ChainedForeignKey(
            FirmLocation,
            chained_field='firm',
            chained_model_field='firm',
            show_all=False,
            auto_choose=True,
            sort=True)

    friends = models.ManyToManyField("self")
    trainees = models.ManyToManyField("self", 
                    through='Training', 
                    related_name="trainers", 
                    symmetrical=False)
    workers = models.ManyToManyField("self", 
                    related_name="supervisors", 
                    symmetrical=False)
    @property
    def full_name(self):
        return f"{self.last_name}, {self.first_name}"

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=exclude)

        qs = self.__class__._default_manager.filter(
            first_name=self.first_name,
            last_name=self.last_name,
            firm_location=self.firm_location    
        )

        if self._state.adding and qs.exists():
            raise ValidationError('The employee already exists.')

    def __str__(self):
        return f'{self.full_name} at {self.firm_location}'

class Organization(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Employee, through='Membership', symmetrical=False)

    def __str__(self):
        return self.name

class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

class Training(models.Model):
    trainer = models.ForeignKey(Employee, related_name='trainee_set', on_delete=models.CASCADE)
    trainee = models.ForeignKey(Employee, related_name='trainer_set', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)