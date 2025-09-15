from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse

from booking.models import Booker, Event
from booking.serializers.bookerSerializer import BookerSerializer


class BookerListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="List bookings of the authenticated user",
        description="Returns all bookings made by the logged-in user.",
        responses={200: BookerSerializer(many=True)},
        tags=['Bookings']
    )
    def get(self, request):
        bookings = Booker.objects.filter(user=request.user)
        serializer = BookerSerializer(bookings, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Book an event",
        description="Create a new booking for an event. Decreases available places automatically.",
        request=BookerSerializer,
        responses={201: BookerSerializer, 400: OpenApiResponse(description="Validation error.")},
        tags=['Bookings']
    )
    def post(self, request):
        serializer = BookerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            booking = serializer.save()
            return Response(BookerSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookerDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Get booking details",
        description="Retrieve details of a specific booking by ID (must belong to the current user).",
        responses={200: BookerSerializer, 404: OpenApiResponse(description="Booking not found.")},
        tags=['Bookings']
    )
    def get(self, request, pk):
        booking = get_object_or_404(Booker, pk=pk, user=request.user)
        serializer = BookerSerializer(booking)
        return Response(serializer.data)
