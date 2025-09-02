from rest_framework.views import APIView
from rest_framework.response import Response
from booking.models import User
from booking.serializers import UserSerializer

class UserView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

  