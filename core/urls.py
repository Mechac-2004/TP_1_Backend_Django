
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
#from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

schema_view = get_schema_view(
    openapi.Info(
        title="Booking Event API",
        default_version='v1.0.0',
        description="Documentation de l'API Booking Events",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0) ),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
