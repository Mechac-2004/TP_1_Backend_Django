# views/user_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema, OpenApiResponse

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group

from booking.models import User
from booking.serializers.userSerializer import (
    RegisterSerializer,
    UserSerializer,
    AdminAssignGroupSerializer,
)
from booking.serializers.userSerializer import CustomTokenObtainPairSerializer
from booking.permissions import IsAdminUserOnly


# --- LOGIN VIEW ---
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @extend_schema(
        summary="User Login (JWT)",
        description="Login using email and password. Returns access & refresh tokens.",
        responses={
            200: OpenApiResponse(description="Login successful. JWT tokens returned."),
            401: OpenApiResponse(description="Invalid credentials."),
        },
        tags=['Users']
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# --- REGISTER VIEW ---
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="User Registration",
        description="Register a new user with email, password, first_name, and last_name.",
        request=RegisterSerializer,
        responses={
            201: UserSerializer,
            400: OpenApiResponse(description="Validation error."),
        },
        tags=['Users']
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- USER PROFILE VIEW ---
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Get Authenticated User Profile",
        description="Returns details of the currently logged-in user, including groups.",
        responses={
            200: UserSerializer,
            401: OpenApiResponse(description="Authentication credentials were not provided."),
        },
        tags=['Users']
    )
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# --- ASSIGN GROUP VIEW (ADMIN ONLY) ---
class AssignGroupView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="Assign Group to User (Admin only)",
        description="Assign a new group to a user by name. Existing groups are removed first.",
        request=AdminAssignGroupSerializer,
        responses={
            200: UserSerializer,
            400: OpenApiResponse(description="Validation error."),
            403: OpenApiResponse(description="Permission denied."),
            404: OpenApiResponse(description="User not found."),
        },
        tags=['Users']
    )
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = AdminAssignGroupSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserListView(APIView):
    """
    Vue pour récupérer la liste des utilisateurs (accessible uniquement par les admins)
    """
    permission_classes = [IsAdminUserOnly]

    @extend_schema(
        summary="Liste des utilisateurs (Admin uniquement)",
        description="Retourne la liste de tous les utilisateurs de la plateforme. Seul un admin peut accéder à ce endpoint.",
        responses={
            200: OpenApiResponse(response=UserSerializer(many=True), description="Liste des utilisateurs"),
            403: OpenApiResponse(description="Accès interdit - Vous n'êtes pas admin")
        },
        tags=['Users']
    )
    def get(self, request):
        users = User.objects.all().order_by("-date_joined")
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
