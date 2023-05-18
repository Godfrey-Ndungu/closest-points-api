from django.test import TestCase
from django.utils import timezone
from api.models import Point


class PointModelTestCase(TestCase):
    def test_create_point(self):
        """
        Test creating a new Point instance.
        """
        x = 2
        y = 2

        point = Point.create(x, y)

        self.assertIsInstance(point, Point)
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)

    def test_point_timestamps(self):
        """
        Test that created_at and updated_at timestamps are set correctly.
        """
        x = 2
        y = 2

        point = Point.create(x, y)

        """
        Test that created_at and updated_at
        timestamps have correct date, hour, minute, and second.
        """
        x = 2
        y = 2

        point = Point.create(x, y)

        current_time = timezone.now()

        self.assertEqual(point.created_at.date(), current_time.date())
        self.assertEqual(point.created_at.hour, current_time.hour)
        self.assertEqual(point.created_at.minute, current_time.minute)
        self.assertEqual(point.created_at.second, current_time.second)
        self.assertEqual(point.updated_at.date(), current_time.date())
        self.assertEqual(point.updated_at.hour, current_time.hour)
        self.assertEqual(point.updated_at.minute, current_time.minute)
        self.assertEqual(point.updated_at.second, current_time.second)
