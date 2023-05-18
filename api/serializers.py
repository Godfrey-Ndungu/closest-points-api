from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.ModelSerializer):
    points = serializers.CharField()

    def validate_points(self, value):
        points = value.split(";")
        if len(points) < 2:
            raise serializers.ValidationError(
                "At least 2 points are required.")
        for point in points:
            coordinates = point.split(",")
            if len(coordinates) != 2:
                raise serializers.ValidationError(
                    "Invalid format. Points must be in the format 'x,y'."
                )
            try:
                x, y = map(int, coordinates)
            except ValueError as e:
                raise serializers.ValidationError(
                    "Invalid point format. Coordinates must be integers."
                ) from e
        return value

    class Meta:
        model = Point
        fields = ("points",)
