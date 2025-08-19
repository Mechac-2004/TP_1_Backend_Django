from django.db import models
from django.contrib.auth.models import AbstractUser


# Classe Utilisateur
class Utilisateur(AbstractUser):
    date_creation = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('client', 'Client'),
            ('administrateur', 'Administrateur')
        ]
    )

    def __str__(self):
        return self.username