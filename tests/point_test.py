"""
Test class for Point
"""
from treevolution.base.geometry import Point

class TestPoint:
    """TestPoint class in order to test Point behavior
    """

    def test_point(self):
        """Test classical point instance
        """
        point = Point(10, 10)
        assert point.x == 10

    def test_point_random(self):
        """Test random created point instance
        """
        point = Point.random(10, 10)
        assert point.x < 10
        
    def test_inside_circle(self):
        """Test if point is inside circle
        """
        point = Point(0.5, 0.5)
        
        circle_center = Point(0, 0)
        assert point.is_inside_circle(circle_center, 1)
        
        point = Point(2, 2)
        assert not point.is_inside_circle(circle_center, 1)
        
    def test_inside_rectangle(self):
        """Test if point is inside rectangle
        """
        
        point = Point(0.5, 0.5)
        
        bottom_left = Point(0, 0)
        upper_right = Point(2, 2)
        
        assert point.is_inside_rectangle(bottom_left, upper_right)
        
        bottom_left = Point(1, 1)
        upper_right = Point(2, 2)

        assert not point.is_inside_rectangle(bottom_left, upper_right)
