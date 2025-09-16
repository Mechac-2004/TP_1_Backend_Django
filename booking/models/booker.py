from django.db import models
from django.core.exceptions import ValidationError
from .user import User
from .event import Event


class Booker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    nbrPlaceReserver = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     # unique_together = ('user', 'event')  # Empêche un user de réserver 2 fois le même event

    def clean(self):
        # Vérifier que l'événement est publié
        if self.event.statut != 'published':
            raise ValidationError("You can't book for an unpublished event.")

        # Vérifier qu'il y a assez de places
        if self.nbrPlaceReserver > self.event.nbPlaceAvailable:
            raise ValidationError("Not enough available places for this booking.")

    def save(self, *args, **kwargs):
        # Décrémenter nbPlaceAvailable dans l'événement
        self.full_clean()  # exécute la validation avant de sauvegarder
        self.event.nbPlaceAvailable -= self.nbrPlaceReserver
        self.event.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.user.email} - "
            f"{self.event.title} - "
            f"{self.nbrPlaceReserver} place(s)"
        )
