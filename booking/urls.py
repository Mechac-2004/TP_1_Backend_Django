from django.urls import path
from booking.views.userView import (
    LoginView,
    RegisterView,
    UserProfileView,
    AssignGroupView,
    UserListView
)
from booking.views.eventView import EventListCreateView, EventDetailView
from booking.views.bookerView import BookerListCreateView, BookerDetailView

urlpatterns = [
    # --- USERS ---
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/profile/", UserProfileView.as_view(), name="user-profile"),
    path("auth/assign-group/<int:pk>/", AssignGroupView.as_view(), name="assign-group"),
    path("users/", UserListView.as_view(), name="user-list"),

    # --- EVENTS ---
    path("events/", EventListCreateView.as_view(), name="event-list-create"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event-detail"),

    # --- BOOKINGS ---
    path("bookings/", BookerListCreateView.as_view(), name="booking-list-create"),
    path("bookings/<int:pk>/", BookerDetailView.as_view(), name="booking-detail"),
]
