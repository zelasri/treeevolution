"""
Module which contains World class
"""
from datetime import datetime, timedelta,date

class World():
    """
    World class in order to represent the forest and simulate the evolution of trees
    """
    def __init__(self, height, width, start_date):
        self._height = height
        self._width = width
        self._start_date = datetime.strptime(str(start_date), "%Y-%m-%d %H:%M:%S")
    
    def step(self,_start_date):
        date= datetime.strptime(str(_start_date), "%Y-%m-%d %H:%M:%S")
        end_date= date + timedelta(days=1)
        return end_date
        
    def date(self):
        return date.today()
    #fix