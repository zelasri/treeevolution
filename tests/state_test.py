"""
Test class for state Enum
"""
from treevolution.models import SeedState, BranchState, TreeState

class TestState:
    """TestState class in order to test enum values
    """

    def test_state(self):
        """Default Enums test
        """
        assert SeedState.ON_BRANCH.name == "ON_BRANCH"
        assert BranchState.INTACT.name == "INTACT"
        assert TreeState.TREE.name == "TREE"
