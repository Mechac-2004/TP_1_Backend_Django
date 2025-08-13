from rest_framework import viewsets
from .models import Utilisateur, Events, Reservation
from .serializers import (
	UtilisateurSerializer,
	EventsSerializer,
	ReservationSerializer,
)


class UtilisateurViewSet(viewsets.ModelViewSet):
	queryset = Utilisateur.objects.all()
	serializer_class = UtilisateurSerializer


class EventsViewSet(viewsets.ModelViewSet):
	queryset = Events.objects.all()
	serializer_class = EventsSerializer


class ReservationViewSet(viewsets.ModelViewSet):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer	


