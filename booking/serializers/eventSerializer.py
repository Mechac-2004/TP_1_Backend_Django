from rest_framework import serializers
from booking.models import Event


class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = ['id', 'title', 'description', 'date', 'lieu', 'nbPlace', 'prix']