"""
Geometry module
"""
import random
import math

class Point():
    """
    Point class structure:
    
    - stores `x` and `y` coordinate (2D representation)
    - can check if point is inside specific rectangle
    - can check if point is inside specific circle
    """

    def __init__(self, x_coord, y_coord):
        """
        Point constructor

        Attributes:
            x: {float} -- the `x` coordinate
            y: {float} -- the `y` coordinate
        """
        self._x = x_coord
        self._y = y_coord

    # pylint: disable=invalid-name
    @property
    def x(self):
        """
        Let access to the `x` property of Point
        
        Returns: 
            {int}: the `x` Point property
        """
        return self._x
    # pylint: enable=invalid-name
    
    # pylint: disable=invalid-name
    @property
    def y(self):
        """
        Let access to the `y` property of Point

        Returns: 
            {int}: the `y` Point property
        """
        return self._y
    # pylint: enable=invalid-name

    @staticmethod
    def random(max_width, max_height):
        """
        Random point constructor
        Initializes point into ([0, max_width], [0, max_height])

        Attributes:
            max_width: {int} -- the upper interval in `x`
            max_height: {int} -- the upper interval in `y`

        Returns:
            {:class:`~treevolution.base.geometry.Point`}: random instance
        """
        return Point(random.uniform(0, max_width), random.uniform(0, max_height)) 

    def is_inside_circle(self, circle_center, radius):
        """
        Check if current point is inside a circle

        Attributes:
            circle_center: {:class:`~treevolution.base.geometry.Point`} -- center point of circle
            radius: {float} -- radius of the circle
        
        Returns: 
            {bool}: True if current point instance is inside
        """
        # pylint: disable=line-too-long
        # resource: https://math.stackexchange.com/questions/198764/how-to-know-if-a-point-is-inside-a-circle
        # pylint: enable=line-too-long
        x_distance = abs(self.x - circle_center.x) * abs(self.x - circle_center.x)
        y_distance = abs(self.y - circle_center.y) * abs(self.y - circle_center.y)
        distance = math.sqrt(x_distance + y_distance)

        return distance < radius

    def is_inside_rectangle(self, point_1, point_2):
        # pylint: disable=line-too-long
        """
        Check if current point is inside a circle

        Attributes:
            point_1: {:class:`~treevolution.base.geometry.Point`} -- left upper corner point of the rectangle
            point_2: {:class:`~treevolution.base.geometry.Point`} -- right down corner point of the rectangle
        
        Returns: 
            {bool}: True if current point instance is inside
        """
        # pylint: disable=line-too-long

        x_coord_1 = point_1.x
        x_coord_2 = point_2.x

        y_coord_1 = point_1.y
        y_coord_2 = point_2.y
        
        if (self.x > x_coord_1 and self.x < x_coord_2 
            and self.y > y_coord_1 and self.y < y_coord_2):
            return True
 
        return False


    def __str__(self):
        """
        `str` representation Point information

        Returns: 
            {str}: expected formated data
        """
        return f"(x: {self._x}, y: {self._y})"
