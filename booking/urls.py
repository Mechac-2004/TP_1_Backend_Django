from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views import EventViewSet, UserView, BookerView, UserDetailView

print("booking urls loaded")

router = DefaultRouter()
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('bookers/', BookerView.as_view(), name='booker'),
    path('users/', UserView.as_view(), name='user'),  
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
]
