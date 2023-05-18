from django.test import TestCase
from django.utils import timezone
from api.models import Point
from api.models import ClosestPoint


class PointModelTest(TestCase):
    def test_create_points(self):
        points = "2,2;-1,30;20,11;4,5"
        new_points = Point.create(points)

        self.assertEqual(new_points.points, points)
        self.assertTrue(new_points.created_at)
        self.assertTrue(
            timezone.now() - new_points.created_at < timezone.timedelta(seconds=1)
        )  # noqa


class ClosestPointModelTest(TestCase):
    def test_create_closest_point(self):
        point_data = "2,2;-1,30;20,11;4,5"
        closest_points_data = "2,2;4,5"
        point = Point.create(point_data)
        closest_point = ClosestPoint.create(
            point=point, closest_points=closest_points_data
        )

        self.assertEqual(closest_point.point, point)
        self.assertEqual(closest_point.closest_points, closest_points_data)
