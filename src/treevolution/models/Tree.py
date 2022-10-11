from abc import abstractmethod
from typing_extensions import Self
from datetime import datetime





class Tree():
    def __init__(self,coordinate,birth,world):
        self.coordinate = coordinate
        self.birth = datetime.strptime(birth, "%Y-%m-%d")
        self.world = world
        self.height = 0
        self.nutrient = 100
        self.fallen = False
        self.age = 0
        self.max_age = None
        self.days_in_humus = None
        self.world = world
    
    def get_height(self):
        return self.height
    
    def get_world(self):
        return self.world
    def get_nutrient(self):
        return self.nutrient
    def get_fallen(self):
        return self.fallen
      
    def get_age(self):
        return self.age

    # setters
    
    def set_height(self,height):
        self.height = height
    
    def set_fallen(self,fallen):
        self.fallen = fallen
    
    @abstractmethod
    def health(self):
        pass

    @abstractmethod
    def width(self):
        pass

    @abstractmethod
    def evolve(self):
        pass

class Oak(Tree):
    MIN_HEIGHT, MAX_HEIGHT = 5, 7
    MIN_AGE, MAX_AGE = 5, 10
    def __init__(self,coordinate,birth,world):
        super(). __init__(coordinate,birth,world)
    def inc_height():
        Self.world.height+=0.005 

    def evolve(self):
        super().evolve()
        
        d1 = self.world.date()
        a = datetime.strptime(str(d1),"%Y-%m-%d")
        d2 = self.world.step(str(d1))
        delay = (d2 - a).days
        if self.height < Oak.MAX_HEIGHT:
                self.height+=0.005


    def health(self):
        super().health(self)
        return self.health

    def width(self):
        super().width()
        return self.get_height() * 0.008
            

            

    
        