from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from . import views

def index_view(request):
    return render(request, 'dist/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('fiction/', include('fiction.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
