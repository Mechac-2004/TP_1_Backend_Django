from rest_framework import serializers
from booking.models import Booker


class BookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ['id', 'user', 'event', 'nbrPlaceReserver', 'date']
        read_only_fields = ['user', 'date']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
