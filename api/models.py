from django.db import models


class Point(models.Model):
    """Model to store a set of points on a grid."""

    created_at = models.DateTimeField(auto_now_add=True)
    points = models.CharField(max_length=255)

    def __str__(self):
        """
        Return a string representation of the Point object.

        :return: String representation of the Point object.
        :rtype: str
        """
        return f"Points: {self.points}"

    @classmethod
    def create(cls, points):
        """
        Create a new Points object.

        :param points: The points as a string.
        :type points: str
        :return: The created Points object.
        :rtype: Points
        """
        new_points = cls(points=points)
        new_points.save()
        return new_points


class ClosestPoint(models.Model):
    """Model to store closestpoints on a grid."""

    point = models.OneToOneField(Point, on_delete=models.CASCADE)
    closest_points = models.CharField(max_length=255)

    @classmethod
    def create(cls, point, closest_points):
        """
        Create a new ClosestPoint object.

        :param points: The associated Points object.
        :type points: Points
        :param closest_points: The closest points as a string.
        :type closest_points: str
        :return: The created ClosestPoint object.
        :rtype: ClosestPoint
        """
        new_closest_point = cls(point=point, closest_points=closest_points)
        new_closest_point.save()
        return new_closest_point
