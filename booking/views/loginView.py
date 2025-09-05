from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Token


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        
        user = authenticate(request, username=email, password=password)
        if not user:
            return Response({"error": "Identifiants invalides"}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, _ = Token.objects.get_or_create(user=user)
        token.generate_tokens()
        
        return Response({
            "access_token": token.access_token,
            "refresh_token": token.refresh_token,
            "expires_in": 900
        })