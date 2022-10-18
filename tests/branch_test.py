"""
Test class for Branch
"""
import random
import pytest
from datetime import datetime

from treevolution.base import Point
from treevolution.world import World
from treevolution.context import Context
from treevolution.models.trees import Oak
from treevolution.models.branches import OakBranch

from treevolution.models import TreeState, tree

class TestBranch:
    """TestBranch class in order to test World behavior
    """
    
    @pytest.fixture
    def world(self):
        """World fixture context for branch test
        """
        random.seed(42)
        w_world, h_world = 200, 200

        current_date = datetime.strptime("2022-09-10", "%Y-%m-%d")
        world = World(current_date, w_world, h_world)
        point = Point.random(w_world, h_world)
        tree = Oak(point, current_date, world)
        
        world.add_tree(tree)
        
        return world

    def test_branch(self, world):
        """S2 - Task 1: Test classical point instance
        """
        current_date = world.date
        _, _, trees, _ = world.state()
        tree = trees[0]
        branch = OakBranch(0, 180, current_date, tree)
        
        for _ in range(20):
            _, weather, _, _ = world.step()
            context = Context(weather, weather.sun, 0)
            branch.evolve(context)
            
        assert branch.length > 0
        assert branch.density > 0
        assert branch.height == 0 # by default
        
    def test_tree_branches(self, world):
        """S2 - Task 2: Test tree number of branches
        """
        
        _, _, trees, _ = world.state()
        tree = trees[0]
        
        for _ in range(3000):
            _, weather, _, _ = world.step()
            context = Context(weather, weather.sun, 0)
            tree.evolve(context)
            
        assert len(tree.branches) == 9
        
        for branch in tree.branches:
            assert branch.length > 0
            
    def test_tree_broken_branches(self, world):
        """S2 - Task 4: Test tree loss of nutrient
        """
 
        _, _, trees, _ = world.state()
        tree = trees[0]
        
        for _ in range(3000):
            world.step()
            
        broken_branches = [ b for b in tree.branches if b.broken ]
        assert len(broken_branches) > 0
        
        branch_ratio = 1 - (len(broken_branches) / len(tree.branches))
        
        if len(tree.branches) > 0:
            
            if tree.state != TreeState.HUMUS:
                assert f"{tree.health:.2f}" == f"{(tree.nutrient * branch_ratio):.2f}"
            else:
                assert tree.health == 0
