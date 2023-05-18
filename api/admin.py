from django.contrib import admin
from .models import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('x', 'y')
