from abc import ABC, abstractmethod
from treevolution.context.context import Context
from treevolution.models.tree import Tree
from dateutil.relativedelta import relativedelta, MO
from treevolution.context.weather import Weather
from treevolution.models.state import TreeState
from treevolution.models.branch import Branch
from treevolution.models.state import BranchState


class Branch(ABC):
    def __init__(self,_height,birth,tree:Tree):
        self._tree = tree
        self._birth = birth
        self._state = BranchState.EVOLVE
        self._lenght = 0
        self._height = _height
        self._max_length =  None
        self._density = 0
        
    @property
    def tree(self):
        return self._tree
    
    @property
    def birth(self):
        return self._birth
    
    @property
    def state(self):
        return self._state
    
    @property
    def lenght(self):
        return self._lenght
    
    @property
    def max_length(self):
        return self._max_length

   
    
    @property
    @abstractmethod
    def health(self):
        pass
    
    @property
    @abstractmethod
    def width(self):
        pass
    
    @abstractmethod
    def evolve(self):
        pass
        
        
    

