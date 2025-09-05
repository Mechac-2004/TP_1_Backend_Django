from rest_framework import serializers
from booking.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["access_token", "refrresh_token", "created_at"]