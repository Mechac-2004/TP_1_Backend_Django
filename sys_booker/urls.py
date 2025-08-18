from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from booker.views_test import EventsApi

schema_view = get_schema_view(
    openapi.Info(
        title="Sys Booker API",
        default_version="v1",
        description="Documentation pour l'API de Sys Booker",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', EventsApi.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include([
        path('', include('booker.urls')),
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='swagger-ui',
        ),
    ])),
]