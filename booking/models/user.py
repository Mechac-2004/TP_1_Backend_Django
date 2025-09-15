from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    
    """Manager personnalisé pour le modèle User."""  
    def create_user(self, email, password=None, **extra_fields):
        
        """Créer un utilisateur classique avec email comme identifiant."""
        if not email:
            raise ValueError("email is required.")
        
        # Normalisation de l'email (minuscule, suppression d'espaces)
        email = self.normalize_email(email)
        
        # Création de l'utilisateur
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash sécurisé du mot de passe
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        
        """Créer un superutilisateur."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    """Modèle d'utilisateur personnalisé basé sur AbstractUser."""
    username = None
    email = models.EmailField(unique=True)
    
    objects = UserManager()

    # Utilisation de l'email comme champ principal pour l'authentification
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email   