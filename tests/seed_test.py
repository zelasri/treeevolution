"""
Test class for Seed
"""
import random
import pytest
from datetime import datetime

from treevolution.base import Point
from treevolution.world import World
from treevolution.context import Weather
from treevolution.models.trees import Oak
from treevolution.models.branches import OakBranch
from treevolution.models.seeds import OakNut
from treevolution.models import SeedState

from treevolution.base.physics import fallen_body_coordinate

class TestSeed:
    """TestBranch class in order to test World behavior
    """

    @pytest.fixture
    def world(self):
        random.seed(42)
        w_world, h_world = 20, 20

        current_date = datetime.strptime("2022-09-10", "%Y-%m-%d")
        current_world = World(current_date, w_world, h_world)
        point = Point.random(w_world, h_world)
        tree = Oak(point, current_date, current_world)
        current_world.add_tree(tree)
        
        return current_world
        
    def test_seed_evolution(self, world):
        """S3 - Task 1: Test classical seed instance and evolve
        """
        current_date, _, trees, _ = world.state()
        tree = trees[0]
                
        for _ in range(100):
            world.step()
            
        branch = OakBranch(0, 180, current_date, tree)
        seed = OakNut(tree, branch, current_date)
        tree.add_branch(branch)
        
        previous_state = seed.state
        
        # end of seed on ground state reached
        for _ in range(100):
            _, weather, _, _ = world.step()
            
            seed.evolve(weather)
                
            if previous_state == SeedState.ON_BRANCH and \
                previous_state != seed.state:
                    
                    # check seed evolution
                    assert seed.state == SeedState.WAITING or \
                        seed.state == SeedState.DEAD or \
                        seed.state == SeedState.EATEN or \
                        seed.state == SeedState.TREE
            
            previous_state = seed.state

    def test_seed_fall_coordinate(self):
        """S3 - Task 4:
        """
        
        current_date = datetime.strptime("2022-09-10", "%Y-%m-%d")
        weather = Weather(current_date, 100, 0, 0, 0)
        
        point = Point(0, 0)
        arrival_point = fallen_body_coordinate(weather, 1.5, point)
        
        assert f"{arrival_point.y:.2f}" > f"{point.y:.2f}"
        assert f"{arrival_point.x:.2f}" == f"{point.x:.2f}"
        
        weather = Weather(current_date, 100, 45, 0, 0)
        
        point = Point(0, 0)
        arrival_point = fallen_body_coordinate(weather, 1.5, point)
        
        assert f"{arrival_point.y:.2f}" > f"{point.y:.2f}"
        assert f"{arrival_point.x:.2f}" > f"{point.x:.2f}"
        
        weather = Weather(current_date, 100, 90, 0, 0)
        
        point = Point(0, 0)
        arrival_point = fallen_body_coordinate(weather, 1.5, point)
        
        assert f"{arrival_point.y:.2f}" == f"{point.y:.2f}"
        assert f"{arrival_point.x:.2f}" > f"{point.x:.2f}"
