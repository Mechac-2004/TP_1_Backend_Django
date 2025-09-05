from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Token

class LogoutView(APIView):
    def post(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return Response({"error": "Token requis"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token_obj = Token.objects.get(access_token=token)
        except Token.DoesNotExist:
            return Response({"error": "Token invalide"}, status=status.HTTP_401_UNAUTHORIZED)

        token_obj.access_token = None
        token_obj.refresh_token = None
        token_obj.save()

        return Response({"message": "Déconnexion réussie"})