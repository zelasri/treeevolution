
from treevolution.models.trees.oak import Oak
from treevolution.context.context import Context
#from treevolution.models.tree import Tree
from treevolution.world import World
from datetime import datetime
from treevolution.context.weather import Weather
from treevolution.base.geometry import Point



class TestTree:
        
    
    def test_tree(self): 
        date = datetime.strptime("2033-08-02 00:00:00", "%Y-%m-%d %H:%M:%S")
        
        weather = Weather(date, 100, 80, 0.4, 0.5)
        context=Context(weather,10,5)
        
        birth= datetime.strptime("2022-08-13 00:00:00","%Y-%m-%d %H:%M:%S")

        #date = datetime.strptime("2022-08-22","%Y-%m-%d")

        world= World(12,10,date)
        assert world._height ==12
        assert world._width == 10
        
        coordinate = Point(10, 10)
        oak= Oak(coordinate, birth, world)
        for i in range (7):
            oak.evolve(context)
        assert oak.height < oak.MAX_HEIGHT
        assert oak._age == oak.MAX_AGE
        
        
        
    



