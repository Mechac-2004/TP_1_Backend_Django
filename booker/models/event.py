from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    nbPlace = models.IntegerField()
    prix = models.FloatField()

    def __str__(self):
        return self.title