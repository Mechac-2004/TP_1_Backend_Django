from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class Command(BaseCommand):
    help = "Crée des utilisateurs de test et les assigne aux groupes par défaut"

    def handle(self, *args, **kwargs):
        # Créer les groupes si besoin
        groups = {g.name: g for g in Group.objects.all()}
        required_groups = ["Client", "Organisateur", "Admin"]
        for name in required_groups:
            if name not in groups:
                groups[name], _ = Group.objects.get_or_create(name=name)

        users_data = [
            {"email": "client@example.com", "password": "password123", "group": "Client"},
            {"email": "orga@example.com", "password": "password123", "group": "Organisateur"},
            {"email": "admin@example.com", "password": "password123", "group": "Admin"},
        ]

        for data in users_data:
            user, created = User.objects.get_or_create(email=data["email"])
            if created:
                user.set_password(data["password"])
                user.save()
                user.groups.add(groups[data["group"]])
                self.stdout.write(self.style.SUCCESS(f"Utilisateur {data['email']} créé dans groupe {data['group']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Utilisateur {data['email']} existe déjà"))
        
        self.stdout.write(self.style.SUCCESS("Utilisateurs par défaut initialisés."))
