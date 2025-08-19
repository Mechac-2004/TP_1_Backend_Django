from rest_framework import serializers
from booker.models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
	class Meta:	
		model = Utilisateur
		fields = ['id', 'username', 'email', 'role', 'date_creation']