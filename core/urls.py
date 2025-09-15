from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # --- API routes ---
    path("api/", include("booking.urls")),

    # --- Swagger & API Docs ---
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]



# from django.contrib import admin
# from django.urls import path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Booking Event API",
#         default_version='v1.0.0',
#         description="Documentation de l'API Booking Events",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('booking/', include('booking.urls')),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0) ),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
# ]
