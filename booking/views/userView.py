from rest_framework.views import APIView
from rest_framework.response import Response
from booking.models import User
from booking.serializers import UserSerializer

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