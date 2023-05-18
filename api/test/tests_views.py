from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Point, ClosestPoint


class PointAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_point_with_valid_data(self):
        url = reverse("closest_point")
        data = {
            "points": "2,2;-1,30;20,11;4,5"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert point creation
        self.assertEqual(Point.objects.count(), 1)
        point = Point.objects.first()
        self.assertEqual(point.points, "2,2;-1,30;20,11;4,5")

        # Assert closest point creation
        self.assertEqual(ClosestPoint.objects.count(), 1)
        closest_point = ClosestPoint.objects.first()
        self.assertEqual(closest_point.closest_points, "2,2;4,5")
        self.assertEqual(closest_point.point, point)

        # Assert response data
        expected_data = {
            "status": "ok",
            "nearest_point": "2,2;4,5"
        }
        self.assertEqual(response.data, expected_data)

    def test_create_point_with_invalid_data(self):
        url = reverse("closest_point")
        data = {
            "points": "2,2;invalid;20,11"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Assert no point or closest point created
        self.assertEqual(Point.objects.count(), 0)
        self.assertEqual(ClosestPoint.objects.count(), 0)

    def test_create_point_with_insufficient_points(self):
        url = reverse("closest_point")
        data = {
            "points": "2,2"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Assert no point or closest point created
        self.assertEqual(Point.objects.count(), 0)
        self.assertEqual(ClosestPoint.objects.count(), 0)
