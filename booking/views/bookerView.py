from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from booking.models import Booker
from booking.permissions import IsAdmin, IsClient
from booking.serializers import BookerSerializer

class BookerView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get(self, request):
        # le client ne voit que ses réservations
        bookers = Booker.objects.filter(user=request.user)
        serializer = BookerSerializer(bookers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BookerAdminView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get(self, request):
        # admin voit toutes les réservations
        bookers = Booker.objects.all()
        serializer = BookerSerializer(bookers, many=True)
        return Response(serializer.data)
