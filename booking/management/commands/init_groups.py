from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Crée les groupes par défaut (Client, Organisateur, Admin)"

    def handle(self, *args, **kwargs):
        groups = ["Client", "Organisateur", "Admin"]
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Groupe '{group_name}' created"))
            else:
                self.stdout.write(self.style.WARNING(f"Groupe '{group_name}' already existe"))
        
        self.stdout.write(self.style.SUCCESS("Groupes par défaut initialisés."))
