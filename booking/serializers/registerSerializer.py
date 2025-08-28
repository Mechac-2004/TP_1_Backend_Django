from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True, 
        required=True
    )
    
    class Meta:
        model = User
        fields = ('email', 'username', 'role', 'password', 'password2')
        extra_kwargs = {
            'role': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        # On extrait le mot de passe du dictionnaire 'validated_data' avant de créer l'utilisateur
        password = validated_data.pop('password')

        # Utilisez create_user qui gère automatiquement le hachage du mot de passe
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password, # On passe le mot de passe à la méthode create_user
            role=validated_data.get('role') # Récupérez le rôle de manière sécurisée
        )
        return user