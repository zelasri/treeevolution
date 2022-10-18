"""
Test class for Tree
"""
import random
import pytest
from datetime import datetime

from treevolution.base import Point
from treevolution.models.state import TreeState
from treevolution.models.trees import Oak
from treevolution.world import World
from treevolution.context import Context, Weather

class TestTree:
    """TestTree class in order to test Tree behavior
    """

    @pytest.fixture
    def world(self):
        random.seed(42)
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        current_world = World(date, 100, 100)
        point = Point.random(current_world.width, current_world.height)
        tree = Oak(point, date, current_world)
        
        current_world.add_tree(tree)
        
        return current_world
        
    def test_tree(self, world):
        """S1 - Task 2: Test classical point instance
        """
        _, _, trees, _ = world.state()
        tree = trees[0] # get current tree
        
        assert tree.age == 0
        assert not tree.fallen
        assert tree.height == 0

    def test_tree_evolve(self, world):
        """S1 - Task 2: Test step method of world instance
        """
        _, _, trees, _ = world.state()
        tree = trees[0] # get current tree
        assert tree.height == 0
        
        for _ in range(5):
            weather = Weather.random(world.date)
            context = Context(weather, weather.sun, 0)
            tree.evolve(context)
            
        assert f'{tree.height}' == f'{(5 * 0.005)}'
        
    def test_tree_evolve_fallen(self, world):
        """S1 - Task 3: Test tree humus state and hence fallen
        """
        _, _, trees, _ = world.state()
        tree = trees[0] # get current tree
        
        assert tree.state == TreeState.TREE
        assert not tree.fallen
        
        # simulate a few number of years (> 10 years)
        for _ in range(4000):
            world.step()
            weather = Weather.random(world.date)
            context = Context(weather, weather.sun, 0)
            tree.evolve(context)
            
        assert tree.state == TreeState.HUMUS
        assert tree.fallen
        
        current_height = tree.height
        
        for _ in range(100):
            world.step()
            weather = Weather.random(world.date)
            context = Context(weather, weather.sun, 0)
            tree.evolve(context)
            
        assert current_height == tree.height

    def test_tree_nutrient(self, world):
        """S1 - Task 6: Test tree loss of nutrient
        """
        _, _, trees, _ = world.state()
        tree = trees[0] # get current tree
        
        for _ in range(3000):
            world.step()
            weather = Weather.random(world.date)
            context = Context(weather, weather.sun, 0)
            tree.evolve(context)
            
        assert tree.health < 100
        

    def test_tree_humus(self, world):
        """S2 - Task 3: Test tree humus bonus
        """
        current_date, _, trees, _ = world.state()
        tree = trees[0] # get current tree
        
        point_neighbor = Point(tree.coordinate.x, tree.coordinate.y + 0.1)
        neighbor = Oak(point_neighbor, current_date, world)
        
        world.add_tree(neighbor)
        
        humus_detected = False
        
        for _ in range(5000):
            _, _, trees, _ = world.step()
            
            # check neighbor always inside
            if neighbor in trees:
                if neighbor != tree and \
                    neighbor.state == TreeState.HUMUS and \
                    tree.state == TreeState.TREE:
                    
                    # expected tree inside        
                    humus_detected = tree.context.humus > 0

        assert humus_detected