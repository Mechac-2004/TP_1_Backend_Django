from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def ensure_permissions_and_groups(sender, **kwargs):
    """
    Ensure that the necessary permissions and groups are created after migrations.
    """

    # Permissions for Client
    try:
        view_event = Permission.objects.get(codename="view_event")
        view_booker = Permission.objects.get(codename="view_booker")
        add_booker = Permission.objects.get(codename="add_booker")
        change_booker = Permission.objects.get(codename="change_booker")
        delete_booker = Permission.objects.get(codename="delete_booker")
        
    except Permission.DoesNotExist:
        # if permissions are not found, exit the function
        return

    # ===  Client's group ===
    client_group, _ = Group.objects.get_or_create(name="Client")
    client_group.permissions.set([
        view_event,
        view_booker,
        add_booker,
        change_booker,
        delete_booker,
       
    ])

    # === Manager's group ===
    organizer_group, _ = Group.objects.get_or_create(name="Organizer")
    organizer_group.permissions.set(Permission.objects.all())

    # === Admin's group ===
    Group.objects.get_or_create(name="Admin")