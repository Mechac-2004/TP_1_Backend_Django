from rest_framework import serializers
from .models import Utilisateur, Events, Reservation


class UtilisateurSerializer(serializers.ModelSerializer):
	class Meta:	
		model = Utilisateur
		fields = ['id', 'username', 'email', 'role', 'date_creation']


class EventsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Events
		fields = ['id', 'title', 'description', 'date', 'lieu', 'nbPlace', 'prix']


class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = ['id', 'utilisateur', 'evenement', 'nbrPlaceReserver', 'date']
		read_only_fields = ['date_reservation']  