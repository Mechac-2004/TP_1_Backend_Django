import secrets
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=64, unique=True, blank=True, null=True)
    refresh_token = models.CharField(max_length=128, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def generate_tokens(self):
        self.access_token = secrets.token_hex(16) # access token (valide 15 min)
        self.refresh_token = secrets.token_hex(32) # refresh token (valide plusieurs jours)
        self.created_at = timezone.now()
        self.save()
        
        
    def is_access_token_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=15)
    
    
    def __str__(self):
        return f"Tokens de {self.user.username}"