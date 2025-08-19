from rest_framework import viewsets
from booker.models import Reservation
from booker.serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer	