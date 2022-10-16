"""
Module which contains World class
"""
from datetime import datetime, timedelta,date
from treevolution.context import Weather
from treevolution.context.context import Context



class World():
    """
    World class in order to represent the forest and simulate the evolution of trees
    """
    def __init__(self, height, width, start_date):
        self._trees = []
        self._height = height
        self._width = width
        self._start_date = datetime.strptime(str(start_date), "%Y-%m-%d %H:%M:%S")
    
    def step(self,_start_date):
        date= datetime.strptime(str(_start_date), "%Y-%m-%d %H:%M:%S")
        end_date= date + timedelta(days=1)
        return end_date
        
    def date(self):
        return date.today()

   
        
    """
        chaque jour un temps météo aléatoire est demandé basé sur la date du jour
    
        def step(self):
        date = datetime.strptime(str(self._start_date), "%Y-%m-%d %H:%M:%S")
        weather = Weather.random(date)
       
        Pour qu’un arbre soit simulé, on
            considère un contexte sans filtre d’éclairage et une quantité de humus fixée à 0.
        
        c = Context( weather,0,0)
        return date ,c.weather(),self._trees

    def last_weather(self):
            l = self.step()
            _ ,weather,_ = l[-1]
            return weather
    
    def consumed(self):
        pass
        """


    