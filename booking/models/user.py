from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('client', 'Client'),
            ('administrateur', 'Administrateur')
        ],
        default='client'
    )

    def __str__(self):
        return self.username