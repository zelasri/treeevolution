"""
Module which contains World class
"""
from datetime import datetime, timedelta,date
from treevolution.models.tree import Tree

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

    def append(self,tree:Tree):
        self._trees.append(tree)
        return self._trees
    def step 
    