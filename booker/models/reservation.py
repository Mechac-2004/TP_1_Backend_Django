from django.db import models
from .utilisateur import Utilisateur
from .event import Event


class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Event, on_delete=models.CASCADE)
    nbrPlaceReserver = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.utilisateur.username} - "
            f"{self.evenement.title} - "
            f"{self.nbrPlaceReserver} places"
        )
