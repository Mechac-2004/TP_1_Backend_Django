from django.db import models
from django.contrib.auth.models import AbstractUser

# Classe Utilisateur
class User(AbstractUser):
    date_creation = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=[('client', 'Client'), ('administrateur', 'Administrateur')])



# Classe Events
class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    nbPlace = models.IntegerField()
    prix = models.FloatField()


# Classe Booker (Réservation)
class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Events, on_delete=models.CASCADE)
    nbrPlaceReserver = models.IntegerField()
    date_reservation = models.DateTimeField(auto_now_add=True)
