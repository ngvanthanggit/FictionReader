from django.urls import path
from . import views

urlpatterns = [
    path('<str:fiction_id>/', views.fiction_page, name="fiction_page"),
    path('<str:fiction_id>/chapter/<str:chapter_id>/', views.chapter_page, name="chapter_page"),
]