
from treevolution.models.trees.oak import Oak
from treevolution.context.context import Context
from treevolution.models.branch import Branch
from treevolution.models.tree import Tree
from treevolution.world import World
from datetime import datetime
from treevolution.context.weather import Weather
from treevolution.base.geometry import Point



class TestBranch:
        
    
    def test_tree(self):
        
        date = datetime.strptime("2033-08-02 00:00:00", "%Y-%m-%d %H:%M:%S")
        
        weather = Weather(date, 100, 80, 0.4, 0.5)
        context=Context(weather,10,5)
        
        birth= datetime.strptime("2022-08-13 00:00:00","%Y-%m-%d %H:%M:%S")

        #date = datetime.strptime("2022-08-22","%Y-%m-%d")

        world= World(12,10,date)
        coordinate = Point(10, 10)
        tre = Tree(coordinate,birth, world)
        B = Branch(1,birth,tre)
        assert B._birth == "2022-08-13 00:00:00","%Y-%m-%d %H:%M:%S"
        
        
        
        
    