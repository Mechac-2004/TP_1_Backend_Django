import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Token
from django.utils import timezone

class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token requis"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token_obj = Token.objects.get(refresh_token=refresh_token)
        except Token.DoesNotExist:
            return Response({"error": "Refresh token invalide"}, status=status.HTTP_401_UNAUTHORIZED)

        token_obj.access_token = secrets.token_hex(16)
        token_obj.created_at = timezone.now()
        token_obj.save()

        return Response({
            "access_token": token_obj.access_token,
            "expires_in": 900
        })
