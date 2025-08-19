from rest_framework import serializers
from booker.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = ['id', 'utilisateur', 'evenement', 'nbrPlaceReserver', 'date']
		read_only_fields = ['date_reservation']  
