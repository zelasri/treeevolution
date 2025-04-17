"""
Test class for Season
"""
from datetime import datetime

from treevolution.context import Season

class TestSeason:
    """TestSeason class in order to test Season behavior
    """

    def test_get(self):
        """Test the get static method of Season
        """
        summer_date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        assert Season.get(summer_date) == Season.SUMMER
        
        fall_date = datetime.strptime("2022-10-10", "%Y-%m-%d")
        assert Season.get(fall_date) == Season.FALL
        
        winter_date = datetime.strptime("2022-12-25", "%Y-%m-%d")
        assert Season.get(winter_date) == Season.WINTER
        
        spring_date = datetime.strptime("2023-04-12", "%Y-%m-%d")
        assert Season.get(spring_date) == Season.SPRING

    def test_to_str(self):
        """Test the to_str method of season
        """
        assert Season.to_str(Season.SUMMER) == "Summer"
        assert Season.to_str(Season.WINTER) == "Winter"
        assert Season.to_str(Season.FALL) == "Fall"
        assert Season.to_str(Season.SPRING) == "Spring"
        assert Season.to_str(6) == "Unknow"
