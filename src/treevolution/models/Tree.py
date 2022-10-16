from abc import ABC, abstractmethod
from treevolution.context.context import Context
from dateutil.relativedelta import relativedelta, MO
from treevolution.context.weather import Weather
from treevolution.models.state import TreeState

class Tree(ABC):
    def __init__(self,coordinate, birth, world):
        self._coordinate = coordinate
        self._birth = birth
        self._world = world
        self._specie = "Tree"
        self._height = 0
        self._nutrient= 100
        self._age= 0
        self._max_age = None
        self._day_in_humus = None
        self._world = world
        self._fallen= False
        
    @property
    def coordinate(self):
        return self.__coordinate
    
    @property
    def world(self):
        return self.__world
    
    @property
    def fallen(self):
        return self._fallen
    
    @property
    def height(self):
        return self._height
    
    @property
    def birth(self):
        return self.__birth

    @height.setter
    def height(self, height):
        self._height = height
        
    @fallen.setter
    def fallen(self, fallen):
        self._fallen = fallen
    
    @property
    @abstractmethod
    def health(self):
        pass
    
    @property
    @abstractmethod
    def width(self):
        pass
    
    @abstractmethod
    def evolve(self, context:Context):
        self._age = relativedelta(context.weather.day, self._birth).years
        
    @property
    def state(self):
        if self._age < self._max_age:
            return TreeState.TREE
        