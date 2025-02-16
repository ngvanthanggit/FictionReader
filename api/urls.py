from django.urls import path

from .views import UserListView, FictionListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('fictions/', FictionListView.as_view(), name='fictions-list'),
]