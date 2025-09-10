from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from booking.models import Event, Booker

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Créer les groupes s'ils n'existent pas
    admin_group, _ = Group.objects.get_or_create(name="Admin")
    client_group, _ = Group.objects.get_or_create(name="Client")

    # Donner tous les droits à Admin
    admin_group.permissions.set(Permission.objects.all())

    # Donner certains droits au Client
    client_permissions = []

    client_permissions += Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Event),
        codename__in=["view_evenement"]
    )
    client_permissions += Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Booker),
        codename__in=["add_reservation", "view_reservation"]
    )

    client_group.permissions.set(client_permissions)
