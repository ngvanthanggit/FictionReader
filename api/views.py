from django.shortcuts import render

from accounts.models import User
from fiction.models import Fiction

from rest_framework import viewsets
from rest_framework import generics
from .serializer import UserSerializer, FictionSerializer

# Create your views here.

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

class FictionListView(generics.ListAPIView):
    serializer_class = FictionSerializer
    
    def get_queryset(self):
        return Fiction.objects.all()