from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views import EventViewSet, UserView, BookerView

print("booking urls loaded")

router = DefaultRouter()
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('booker/', BookerView.as_view(), name='booker'),
    path('user/', UserView.as_view(), name='user'),  
]
