"""
Test class for World
"""
import random
import pytest
from datetime import datetime

from treevolution.base import Point
from treevolution.world import World
from treevolution.models.trees import Oak

class TestWorld:
    """TestWorld class in order to test World behavior
    """
    
    @pytest.fixture
    def world(self):
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        current_world = World(date, 100, 100)
        return current_world

    @pytest.fixture
    def mini_world(self):
        date = datetime.strptime("2022-08-22", "%Y-%m-%d")
        current_world = World(date, 3, 3)
        return current_world

    def test_world(self, world):
        """S1 - Task 1: Test classical point instance
        """
        assert world.height == 100
        assert world.width == 100

    def test_world_step(self, world):
        """S1 - Task 1: Test step method of world instance
        """
        
        for _ in range(5):
            world.step()
            
        expected_date = datetime.strptime("2022-08-27", "%Y-%m-%d")
        assert world.date == expected_date
        
    def test_world_with_trees(self, world):
        """S1 - Task 4: Test step method with some tree instances
        """
        random.seed(42)
        start_date = world.date
        
        _, _, trees, _ = world.state()
        
        assert len(trees) == 0

        trees_at_begin = []
        # create trees
        for _ in range(2):
            point = Point.random(world.width, world.height)
            tree = Oak(point, start_date, world)

            trees_at_begin.append(tree)
            world.add_tree(tree)

        # simulate 1000 days    
        for _ in range(1000):
            
            day, _, _, _ = world.step()
            
        expected_date = datetime.strptime("2025-05-18", "%Y-%m-%d")
        
        assert expected_date == day
        
        for tree in trees_at_begin:
            assert tree.age == 2

    def test_world_removed_trees(self, world):
        """S1 - Task 5: Test remove of trees inside world when fallen
        """
        random.seed(42)

        current_date = world.date

        # create trees
        point = Point.random(world.width, world.height)
        tree = Oak(point, current_date, world)
        
        _, _, trees, _ = world.state()
        
        assert len(trees) == 0

        world.add_tree(tree)
        
        _, _, trees, _ = world.state()
        
        assert len(trees) == 1

        # simulate 1000 days    
        for _ in range(100):
            
            _, _, trees, _ = world.step()
            
        assert len(trees) == 1
        
        for _ in range(2000):
            
            _, _, trees, _ = world.step()
            
        assert tree not in trees


    def test_world_sun_for_trees(self, mini_world):
        """S2 - Task 5: Test filtered sun intensity
        """
        random.seed(0)
        current_date = mini_world.date

        # create trees
        for _ in range(2):
            point = Point.random(mini_world.width, mini_world.height)
            tree = Oak(point, current_date, mini_world)

            mini_world.add_tree(tree)

        # simulate 1000 days    
        for _ in range(3000):
            
            _, weather, trees, _ = mini_world.step()
            
            for tree in trees:            
                
                neighbor_found = None

                for neighbor in trees:

                    if neighbor != tree:
                        
                        # check number of branches
                        n_branches_higher = [b for b in neighbor.branches if b.height > tree.height ]
                        
                        if len(n_branches_higher) > 0 and \
                            tree.coordinate.is_inside_circle(neighbor.coordinate, neighbor.radius):
                            
                            neighbor_found = neighbor
                            break
                            
                if neighbor_found is not None:
                    assert weather.sun >= tree.context.energy
                 
                 
    def test_world_seed_presence_in_branch(self, world):
        """S3 - Task 2: Seed presence inside branch
        """
        random.seed(42)
        
        current_date = world.date

        # create tree
        point = Point.random(world.width, world.height)
        tree = Oak(point, current_date, world)

        world.add_tree(tree)

        has_seeds = False
        # simulate 1000 days    
        for _ in range(2000):
            
            world.step()
            n_seeds = sum([ len(b.seeds) for b in tree.branches ])
            if n_seeds > 0:
                has_seeds = True
            
        assert has_seeds
        
    def test_world_seed_presence_in_world(self, world):
        """S3 - Task 3: Seed presence inside world
        """
        random.seed(42)
        
        current_date = world.date

        # create tree
        point = Point.random(world.width, world.height)
        tree = Oak(point, current_date, world)

        world.add_tree(tree)

        has_seeds = False
        
        # simulate 1000 days    
        for _ in range(2000):
            
            _, _, _, seeds = world.step()
            
            if len(seeds) > 0:
                has_seeds = True
            
        assert has_seeds
