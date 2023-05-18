from django.urls import path
from .views import PointAPIView

urlpatterns = [
    path("closest-point/", PointAPIView.as_view(), name="closest_point")]
