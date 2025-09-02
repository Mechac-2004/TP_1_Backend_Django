from rest_framework.views import APIView
from rest_framework.response import Response
from booking.models import User
from booking.serializers import UserSerializer
from rest_framework import status

class UserView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({"message": "User created successfully."}, status=201)
        else:
            return Response(user.errors, status=400)
        
class UserDetailView(APIView):
    # La méthode get_object sert à récupérer un utilisateur dans la base de données
    # grâce à son identifiant (id), et dans le cas où il n’existe pas on retoune none.

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
        
    # La méthode put sert à modifier un utilisateur dans la base de données
    # grâce à son identifiant (id), et dans le cas où il n’existe pas on retourne 
    # un message d'erreur.
    def put(self, request, id):
        # Ici on récupère un user spécifique
        user = self.get_object(id)

        # Si il n'exist pas on retourne une erreur, sinon on serialize la donnée à modifier
        if not user:
            return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
        
            serializer = UserSerializer(user, data=request.data, partial=True)  
        # On fait la modification et on save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # La méthode delete sert à supprimer un utilisateur dans la base de données
    # grâce à son identifiant (id), et dans le cas où il n’existe pas on retourne 
    # un message d'erreur.
    def delete(self, request, id):
        user = self.get_object(id)
        if not user:
            return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response({'message': 'Utilisateur supprimé avec succès'}, status=status.HTTP_204_NO_CONTENT)
        
