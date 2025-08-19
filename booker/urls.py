from django.urls import include, path
from booker.views import utilisateurView, eventView, reservationView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', utilisateurView)
router.register(r'events', eventView)
router.register(r'reservations', reservationView)	

urlpatterns = [
	path('', include(router.urls)),	
]	