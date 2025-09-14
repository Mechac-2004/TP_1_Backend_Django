from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from .user import User


class Event(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
        ('archived', 'Archivé'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    nbPlace = models.PositiveIntegerField()
    nbPlaceAvailable = models.PositiveIntegerField(editable=False)
    prix = models.FloatField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    def clean(self):
        # Empêcher un utilisateur qui n'est pas Admin/Organisateur de créer un event
        if not (self.user.groups.filter(name__in=['Organisateur', 'Admin']).exists()):
            raise ValidationError("Seuls les organisateurs ou admins peuvent créer un événement.")

        # La date doit être dans le futur
        if self.date < timezone.now():
            raise ValidationError("La date de l'événement doit être dans le futur.")

    def save(self, *args, **kwargs):
        # Si nbPlaceAvailable n'est pas défini, on l'initialise avec nbPlace
        if self._state.adding:  # uniquement à la création
            self.nbPlaceAvailable = self.nbPlace
        else:
            # Vérifier que nbPlaceAvailable ne dépasse pas nbPlace
            if self.nbPlaceAvailable > self.nbPlace:
                self.nbPlaceAvailable = self.nbPlace
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%Y-%m-%d')})"
