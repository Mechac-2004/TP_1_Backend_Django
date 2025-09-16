from django.shortcuts import render
from .bookerView import BookerListCreateView, BookerDetailView
from .eventView import EventListCreateView, EventDetailView
from .userView import LoginView, RegisterView, UserProfileView, AssignGroupView, UserListView