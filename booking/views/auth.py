from email.headerregistry import Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from booking.serializers import RegisterSerializer
from booking.models import User



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Ajouter automatiquement l'utilisateur dans le groupe "Client"
            try:
                client_group = Group.objects.get(name="Client")
                user.groups.add(client_group)
            except Group.DoesNotExist:
                return Response(
                    {"error": "Le groupe Client n'existe pas. Crée-le dans l'admin Django."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response({"message": "Utilisateur créé avec succès"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Email ou Mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        if not check_password(password, user.password):
            return Response({"error": "Email ou Mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)

        # Générer token JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
