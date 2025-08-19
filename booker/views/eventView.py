from rest_framework import viewsets
from booker.models import Event
from booker.serializers import EventSerializer

class EventView(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer