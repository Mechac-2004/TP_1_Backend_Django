from rest_framework import serializers
from booking.models import User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'password', 'date_joined', 'role']