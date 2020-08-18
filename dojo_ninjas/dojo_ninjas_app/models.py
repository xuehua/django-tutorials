from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(blank=True, null=True, default="old dojo")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dojo_detail", kwargs={"pk": self.pk})

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("ninja_detail", kwargs={"pk": self.pk})
