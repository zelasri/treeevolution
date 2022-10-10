"""
Test class for Season
"""
from datetime import datetime,date

from treevolution import World

class TestWorld:
    """Test class in order to test Season behavior
    """
    def test_World(self):

        
        world = World(80, 70,"2022-08-22")
        assert world.height == 80
        assert world.width == 70
        assert str(world.start_date) == "2022-08-22 00:00:00"

    def test_step(self):
        w1 = World(80, 70,"2022-08-10")
        assert str(w1.step("2022-08-09")) == "2022-08-10 00:00:00"

    def date_test(self):
         w1 = World(80, 70,"2022-08-10")
         assert w1.date() == date.today()

