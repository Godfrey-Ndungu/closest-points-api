from django.contrib import admin
from .models import Point
from .models import ClosestPoint


class PointAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "points")
    list_filter = ("created_at",)
    search_fields = ("points",)


class ClosestPointAdmin(admin.ModelAdmin):
    list_display = ("id", "point", "closest_points")
    search_fields = ("points__point", "closest_points")


admin.site.register(ClosestPoint, ClosestPointAdmin)
admin.site.register(Point, PointAdmin)
