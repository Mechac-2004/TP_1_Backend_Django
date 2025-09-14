from rest_framework import serializers
from booking.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'lieu',
            'nbPlace',
            'nbPlaceAvailable',
            'prix',
            'statut',
            'user'
        ]
        read_only_fields = ['nbPlaceAvailable', 'user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
