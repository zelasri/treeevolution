"""
Define all evolution state
"""
from enum import Enum

class SeedState(Enum):
    """
    Define the different state of seed
    - depending of specie, state probability changed
    """
    ON_BRANCH = 1
    WAITING = 2
    DEAD = 3
    EATEN = 4
    TREE = 5


class BranchState(Enum):
    """
    Define the different state of branch
    - depending of specie, state probability changed
    """
    INTACT = 1
    BROKEN = 2
    EVOLVE = 3


class TreeState(Enum):
    """
    Define TreeState (can be tree or dead)
    """
    TREE = 1
    HUMUS = 2
