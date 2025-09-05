from rest_framework import serializers
from booking.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # le champ password est caché en lecture
    

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'role']
        extra_kwargs = {"password": {"write_only": True}}
    
    def	create(self, validated_data):
        password = validated_data.pop("password")	# On retire le champ password de validated_data.
        user = User(**validated_data)				# On crée une instance de User avec les données restantes par déstructuration
        user.set_password(password)					# hashage du mot de passe par la méthode set_pawwsord de AbstractUser
        user.save()
        return user