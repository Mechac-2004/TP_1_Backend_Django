from rest_framework import serializers
from booking.models import Booker

class BookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ['id', 'user', 'event', 'nbrPlaceReserver', 'date']
        read_only_fields = ['user', 'date']  # user et date sont assignés automatiquement

    def create(self, validated_data):
        user = self.context['request'].user
        # Création de la réservation avec l'utilisateur connecté
        return Booker.objects.create(user=user, **validated_data)
