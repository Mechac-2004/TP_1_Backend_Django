from rest_framework import serializers
from booking.models import Booker


class BookerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Booker
		fields = ['id', 'user', 'event', 'nbrPlaceReserver', 'date']