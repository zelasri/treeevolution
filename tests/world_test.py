"""
Test class for Season
"""
from datetime import datetime,date

from treevolution import World

class TestWorld:
    """Test class in order to test Season behavior
    """
    def test_World(self):
        world = World(90, 71, "2022-10-10 00:00:00")
        assert world._height == 90
        assert world._width == 71
        assert str(world._start_date) == "2022-10-10 00:00:00"

    def test_step(self):
        world1 = World(90, 70, "2022-08-10 00:00:00")
        assert str(world1.step("2022-10-15 00:00:00")) == "2022-10-16 00:00:00"

    def date_test(self):
         w1 = World(80, 70,"2022-08-10 00:00:00")
         assert w1.date() == date.today()

