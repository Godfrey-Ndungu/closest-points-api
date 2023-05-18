from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Point, ClosestPoint
from .utils import ClosestPointCalculator

class ClosestPointAPIView(APIView):
    """
    API view for calculating and saving the closest points.
    """

    def post(self, request):
        """
        Calculate the closest points and save the results.

        Input: 
        {
            "points": "x1,y1;x2,y2;x3,y3;..."
        }

        Returns:
        {
            "message": "OK",
            "closest_points": [
                {
                    "point": {
                        "x": <x-coordinate>,
                        "y": <y-coordinate>
                    },
                    "closest_point": {
                        "x": <x-coordinate>,
                        "y": <y-coordinate>
                    }
                },
                ...
            ]
        }
        """
        points_str = request.data.get('points')

        # Separate the points
        points = points_str.split(';')

        if len(points) < 2:
            return Response({"message": "At least two points are required."}, status=400)

        # Save the points in the Point model
        saved_points = []
        for point in points:
            x, y = point.split(',')
            saved_point = Point.create(int(x), int(y))
            saved_points.append(saved_point)

        # Calculate the closest points
        closest_points = []
        for i in range(len(saved_points)):
            for j in range(i + 1, len(saved_points)):
                point = saved_points[i]
                closest_point = saved_points[j]
                ClosestPoint.create(point, closest_point)
                closest_points.append({
                    "point": {
                        "x": point.x,
                        "y": point.y
                    },
                    "closest_point": {
                        "x": closest_point.x,
                        "y": closest_point.y
                    }
                })

        return Response({"message": "OK", "closest_points": closest_points})
