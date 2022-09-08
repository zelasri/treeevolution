"""
Test class for Weather class
"""
from datetime import datetime

from treevolution.context import Weather

class TestWeather:
    """TestWeather class in order to test Weather behavior
    """

    def test_weather(self):
        """Test the constructor method of Weather
        """
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        
        weather = Weather(date, 100, 80, 0.4, 0.5)
        
        assert weather.wind_speed == 100
        assert weather.wind_angle == 80
        assert weather.sun == 0.4
        assert weather.humidity == 0.5

    def test_from_date(self):
        """Test the random static method of Weather
        """
        
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        weather = Weather.random(date)
        
        assert weather.wind_speed >= 0
        assert weather.wind_angle >= 0
        assert weather.wind_angle <= 360
        
        # expected Summer season
        assert weather.sun >= 0.3
        assert weather.humidity >= 0

        date = datetime.strptime("2022-12-22", "%Y-%m-%d")
        weather = Weather.random(date)
        
        # expected Winter season
        assert weather.sun >= 0.1
        assert weather.humidity >= 0.2
