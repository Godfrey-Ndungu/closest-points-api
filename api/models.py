from django.db import models


class Point(models.Model):
    """
    Represents a point on a grid with timestamped capabilities.
    """

    x = models.IntegerField()
    y = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def create(cls, x, y):
        """
        Creates a new Point instance with the given coordinates.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.

        Returns:
            Point: The newly created Point instance.
        """
        point = cls(x=x, y=y)
        point.save()
        return point


class ClosestPoint(models.Model):
    """
    Represents the closest points to a given point on a grid.
    """

    point = models.OneToOneField(Point, on_delete=models.CASCADE)
    closest_point = models.OneToOneField(
        Point, related_name="closest_to", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"ClosestPoint(Point: {self.point}, Closest Point: {self.closest_point})"  # noqa

    @classmethod
    def create(cls, point, closest_point):
        """
        Creates a new ClosestPoint instance with
        the given point and closest_point.

        Args:
            point (Point): The reference point.
            closest_point (Point): The closest point to the reference point.

        Returns:
            ClosestPoint: The newly created ClosestPoint instance.
        """
        closest_point = cls(point=point, closest_point=closest_point)
        closest_point.save()
        return closest_point
