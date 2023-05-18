from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .utils import ClosestPointFinder
from .serializers import PointSerializer

from .models import Point
from .models import ClosestPoint


class PointAPIView(GenericAPIView):
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
