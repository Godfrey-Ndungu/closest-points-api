from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .utils import ClosestPointFinder
from .serializers import PointSerializer

from .models import Point
from .models import ClosestPoint


class PointAPIView(GenericAPIView):
    """
        API endpoint to create a Point and calculate the closest point.

        The API expects a POST request with the following data:
        - points: A string of points in the format 'x1,y1;x2,y2;x3,y3;...'.
                At least 2 points are required.

        Example usage:
        POST /api/points/
        {
            "points": "2,2;-1,30;20,11;4,5"
        }

        Response format:
        {
            "status": "ok",
            "nearest_point": "2,2;4,5"
        }
    """

    serializer_class = PointSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        points = serializer.validated_data["points"]

        point = Point.create(points=points)
        # Calculate nearest point
        closest_points = ClosestPointFinder.find_closest_point(points)

        ClosestPoint.create(closest_points=closest_points, point=point)

        response_data = {"status": "ok", "nearest_point": closest_points}
        return Response(response_data)
