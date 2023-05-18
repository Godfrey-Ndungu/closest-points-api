import math


class ClosestPointFinder:
    @staticmethod
    def parse_point(point_string):
        """
        Parse the point string into coordinates.

        :param point_string: Point string in the format "x,y".
        :type point_string: str
        :return: Tuple representing the coordinates (x, y).
        :rtype: tuple
        """
        x, y = map(float, point_string.split(","))
        x = str(x).rstrip("0").rstrip(".")  # Remove trailing zeros and dot
        y = str(y).rstrip("0").rstrip(".")  # Remove trailing zeros and dot
        return x, y

    @staticmethod
    def calculate_distance(point1, point2):
        """
        Calculate the Euclidean distance between two points.

        :param point1: First point (x1, y1).
        :type point1: tuple
        :param point2: Second point (x2, y2).
        :type point2: tuple
        :return: The Euclidean distance between the points.
        :rtype: float
        """
        x1, y1 = map(float, point1)
        x2, y2 = map(float, point2)
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def find_closest_point(point_string):
        """
        Find the closest pair of points from a given set of points.

        :param point_string: String containing points separated
            by semicolons, e.g., "2,2;-1,30;20,11;4,5".
        :type point_string: str
        :return: String representing the closest pair
            of points in the format "x,y;x,y".
        :rtype: str
        """
        points = [ClosestPointFinder.parse_point(p) for p in point_string.split(";")] # noqa

        if len(points) < 2:
            raise ValueError("At least two points are required.")

        closest_point = None
        min_distance = float("inf")

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = ClosestPointFinder.calculate_distance(points[i], points[j]) # noqa
                if distance < min_distance:
                    min_distance = distance
                    closest_point = (points[i], points[j])

        return ";".join([f"{x},{y}" for x, y in closest_point])
