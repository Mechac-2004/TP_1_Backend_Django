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


# Classe Events
class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    nbPlace = models.IntegerField()
    prix = models.FloatField()

    def __str__(self):
        return self.title


# Classe Booker (Réservation)
class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Events, on_delete=models.CASCADE)
    nbrPlaceReserver = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.utilisateur.username} - "
            f"{self.evenement.title} - "
            f"{self.nbrPlaceReserver} places"
        )
