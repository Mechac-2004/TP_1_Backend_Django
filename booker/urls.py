from django.urls import include, path
from .views import UtilisateurViewSet, EventsViewSet, ReservationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UtilisateurViewSet)
router.register(r'events', EventsViewSet)
router.register(r'reservations', ReservationViewSet)	

urlpatterns = [
	path('', include(router.urls)),	
]	