from rest_framework import viewsets
from booker.models import Utilisateur 
from booker.serializers import UtilisateurSerializer


class UtilisateurViewSet(viewsets.ModelViewSet):
	queryset = Utilisateur.objects.all()
	serializer_class = UtilisateurSerializer