from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title = "Fiction Reader API",
        default_version = '1.0.0',
        description = "API for Fiction Reader",
        public = True,
    )
)

def index_view(request):
    return render(request, 'dist/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('fiction/', include('fiction.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search.urls')),
    path('api/', 
        include([
            path('', include(('api.urls', 'api'), namespace='api')),
            path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
        ])
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
