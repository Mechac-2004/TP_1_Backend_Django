from rest_framework import viewsets, permissions
from booking.models import Event
from booking.serializers import EventSerializer
from booking.permissions import IsAdminOrReadOnly

class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Event.objects.all()     
    serializer_class = EventSerializer