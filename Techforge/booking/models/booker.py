from django.db import models
from .user import User
from .event import Event

class Booker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    nbrPlaceReserver = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.event.title} - "
            f"{self.nbrPlaceReserver} places"
        )