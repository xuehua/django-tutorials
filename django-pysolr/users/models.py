from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class Contact(models.Model):
    user_from = models.ForeignKey('users.CustomUser', 
                related_name = 'rel_from_set',
                on_delete = models.CASCADE)
    user_to = models.ForeignKey('users.CustomUser',
                related_name = 'rel_to_set',
                on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                db_index= True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', 
                blank=True,
                through=Contact,
                related_name='followers',
                symmetrical=False)
