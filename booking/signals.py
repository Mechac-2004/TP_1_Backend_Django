from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from booking.models import Event, Booker

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Groupe Admin
    admin_group, _ = Group.objects.get_or_create(name="Admin")

    # Groupe Client
    client_group, _ = Group.objects.get_or_create(name="Client")

    # Permissions par défaut de Django (CRUD sur tous les modèles)
    all_permissions = Permission.objects.all()
    admin_group.permissions.set(all_permissions)  # admin = tous les droits

    # Permissions spécifiques pour client
    client_permissions = []

    # Ex: Client peut voir les événements
    client_permissions += Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Event),
        codename__in=["view_evenement"]
    )

    # Ex: Client peut réserver
    client_permissions += Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Booker),
        codename__in=["add_reservation", "view_reservation"]
    )

    client_group.permissions.set(client_permissions)
