from rest_framework import viewsets
from booking.models import Event
from booking.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()     
    serializer_class = EventSerializer