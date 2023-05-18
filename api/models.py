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
