from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):
    """
    Autorise uniquement les Organisateurs, Admins ou superusers.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_superuser
                or request.user.groups.filter(name__in=['Organizer']).exists()
            )
        )