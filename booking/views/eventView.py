from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse

from booking.models import Event
from booking.serializers.eventSerializer import EventSerializer


class EventListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="List all published events",
        description="Returns a list of all published events.",
        responses={200: EventSerializer(many=True)},
        tags=['Events']
    )
    def get(self, request):
        events = Event.objects.filter(statut='published')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Create a new event (Organisateur/Admin only)",
        description="Create a new event. Only users in Organisateur or Admin group can create.",
        request=EventSerializer,
        responses={201: EventSerializer, 400: OpenApiResponse(description="Validation error.")},
        tags=['Events']
    )
    def post(self, request):
        serializer = EventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            event = serializer.save()
            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Get event detail",
        description="Get detailed information about a specific event by ID.",
        responses={200: EventSerializer, 404: OpenApiResponse(description="Event not found.")},
        tags=['Events']
    )
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
