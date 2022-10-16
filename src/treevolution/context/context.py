"""
Module context which contains Context class for tree growth
"""

class Context():
    """
    Context class which describes the growth context for the tree
    """

    def __init__(self, weather, sun_intensity, humus):
        # pylint: disable=line-too-long
        """
        Context constructor

        Attributes:
            weather: {:class:`~treevolution.context.weather.Weather`} -- the current day weather
            sun_intensity: {int} -- the perceived sun intensity by the tree depending of its neighborhood and weather
            humus: {int} -- humus quantity enable for tree
        """
        # pylint: enable=line-too-long
        self._weather = weather
        self._sun_intensity = sun_intensity
        self._humus = humus

    @property
    def weather(self):
        """
        Let access to the `weather` property of Context
        
        Returns: 
            {int}: the `weather` Context property
        """
        return self._weather

    @property
    def humus(self):
        """
        Let access to the `humus` property of Context
        
        Returns: 
            {int}: the `humus` Context property
        """
        return self._humus

    @property
    def energy(self):
        """
        Let access to the `energy` property of Context
        The perceived sun intensity for the tree
        
        Returns: 
            {int}: the `energy` Context property
        """
        return self._sun_intensity
 #fix