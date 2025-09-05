from rest_framework.views import APIView
from rest_framework.response import Response
from booking.models import User
from booking.serializers import UserSerializer
from booking.auth import CustomTokenAuthentication
from booking.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

  