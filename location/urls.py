from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView

urlpatterns = [
    # path("", include("api.urls")),
    path("admin/", admin.site.urls),
    path('api/schema/',
         SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
