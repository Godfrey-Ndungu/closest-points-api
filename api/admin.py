from django.contrib import admin
from .models import Point
from .models import ClosestPoint


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ("x", "y", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("x", "y")


@admin.register(ClosestPoint)
class ClosestPointAdmin(admin.ModelAdmin):
    list_display = ('point', 'closest_point')
    search_fields = ('point__x', 'point__y',
                     'closest_point__x', 'closest_point__y')
