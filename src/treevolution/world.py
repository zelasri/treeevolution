"""
Module which contains World class
"""
from datetime import datetime, timedelta,date

class World():
    """
    World class in order to represent the forest and simulate the evolution of trees
    """
    def __init__(self,height,width,start_date):
        self.height = height
        self.width = width
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    def step(self,start_date):
        date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = date + timedelta(days=1)
        return end_date
        
    def date(self):
        return date.today()
    