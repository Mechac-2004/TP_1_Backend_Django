from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from booking.models import Booker
from booking.serializers import BookerSerializer

class BookerView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        bookers = Booker.objects.all()
        serializer = BookerSerializer(bookers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

