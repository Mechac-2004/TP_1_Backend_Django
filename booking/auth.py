from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token


class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return None # pas de token → l'accès sera refusé par DRF
        
        try:
            token_obj = Token.objects.get(access_token=token)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid access token")
        
        if token_obj.is_access_token_expired():
            raise AuthenticationFailed("Expired access token")
        
        return (token_obj.user, None)