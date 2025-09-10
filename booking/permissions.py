from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Client").exists()


class IsAdminOrReadOnly(BasePermission):

    # - Admin (groupe "Admin") => tous les droits (GET, POST, PUT, DELETE)
    #- Client => seulement lecture (GET, HEAD, OPTIONS)
    def has_permission(self, request, view):
        # Lecture seule => tout utilisateur authentifié peut lire
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated  

        # Sinon, seulement Admin peut modifier
        return request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()