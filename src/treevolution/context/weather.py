"""
Module with classes for weather management of each day
"""
import random

class Season():
    """
    Season class with only utils methods
    """

    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4

    @staticmethod
    def get(current_date):
        """
        Get the current season for a specific date

        Attributes:
            current_date: {date} -- expected date to find season
        
        Returns: 
            {int}: the found current Season value
        """

        current_day = current_date.timetuple().tm_yday

        # ranges for the northern hemisphere
        spring_days = range(80, 172)
        summer_days = range(172, 264)
        fall_days = range(264, 355)
        # winter = everything else

        if current_day in spring_days:
            return Season.SPRING

        if current_day in summer_days:
            return Season.SUMMER

        if current_day in fall_days:
            return Season.FALL
        
        # last case
        return Season.WINTER

    @staticmethod
    def to_str(season):
        """
        Give the `str` representation of an enum season value

        Attributes:
            season: {int} -- season value to display
        
        Returns: 
            {str}: str representation of season value
        """

        if season == Season.SPRING:
            return "Spring"
        if season == Season.SUMMER:
            return "Summer"
        if season == Season.FALL:
            return "Fall"
        if season == Season.WINTER:
            return "Winter"
        
        return "Unknow"

class Weather():
    """
    Class which contains the weather of specific date
    """

    MEAN_SPEED = 80
    MAX_SPEED = 160

    # pylint: disable=too-many-arguments
    def __init__(self, day, wind_speed, wind_angle, sun, humidity):
        """
        Weather constructor with parameters

        Attributes:
            day: {date} -- specific weather date
            wind_speed: {float} -- weather wind speed
            wind_angle: {float} -- weather wind direction (all during the day)
            sun: {float} -- sun percentage intensity in [0, 1]
            humidity: {float} -- percent of humidity during the day in [0, 1]
        """
        self._day = day
        self._wind_speed = wind_speed
        self._wind_angle = wind_angle
        self._sun = sun
        self._humidity = humidity
    # pylint: enable=too-many-arguments
        
    @staticmethod
    def random(current_date):
        """
        Static method which retuns semi-random weather for specific date

        Attributes:
            current_date: {date} -- expected date to generate weather
        
        Returns:
            {:class:`~treevolution.context.weather.Weather`}: random weather for specific date
        """
        
        wind_speed = random.weibullvariate(Weather.MEAN_SPEED, 2)

        # wind speed in at least to be >= 0
        wind_speed = max(wind_speed, 0)
        wind_speed = min(wind_speed, Weather.MAX_SPEED)
        
        # random wind direction
        wind_angle = random.random() * 360

        season = Season.get(current_date)
        # depending of season increase or descrease sun intensity
        if season in [Season.SPRING, Season.SUMMER]:
            sun = random.uniform(0.3, 0.6)
        else:
            sun = random.uniform(0.1, 0.3)

        # depending of season increase or descrease humidity
        if season in [Season.SPRING, Season.SUMMER]:
            humidity = random.uniform(0, 0.2)
        else:
            humidity = random.uniform(0.2, 0.5)

        return Weather(current_date, wind_speed, wind_angle, sun, humidity)
   
    @property
    def day(self):
        """
        Let access to the `day` property of Weather
        
        Returns:
            {int}: the `day` Weather property
        """
        return self._day

    @property
    def wind_speed(self):
        """
        Let access to the `wind_speed` property of Weather
        
        Returns:
            {int}: the `wind_speed` Weather property
        """
        return self._wind_speed

    @property
    def wind_angle(self):
        """
        Let access to the `wind_angle` property of Weather
        
        Returns:
            {int}: the `wind_angle` Weather property
        """
        return self._wind_angle

    @property
    def sun(self):
        """
        Let access to the `sun` property of Weather

        Returns:
            {int}: the `sun` Weather property
        """
        return self._sun

    @property
    def humidity(self):
        """
        Let access to the `humidity` property of Weather

        Returns:
            {int}: the `humidity` Weather property
        """
        return self._humidity

    def __str__(self):
        """
        `str` representation of Weather information

        Returns:
            {str}: expected formated data
        """
        return f"(speed: {self._wind_speed:.2f}, angle: {self._wind_angle:.2f}, "\
            f"sun: {self._sun:.2f}, humidity: {self._humidity:.2f})"
