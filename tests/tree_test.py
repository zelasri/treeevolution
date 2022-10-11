from treevolution.models.Tree import Tree
from treevolution.models.Tree import Oak
from treevolution.models.Tree import Oak
from treevolution.world  import World
from treevolution.base.geometry import Point
IN_HEIGHT, MAX_HEIGHT = 5, 7
MIN_AGE, MAX_AGE = 5, 10
class TestTree:

    def test_Tree(self):
        w1= World(81,17,"2022-02-22")
        p1= Point(1,3)
        T1 = Tree(p1,"2022-02-22",w1)
        assert T1.world.height == 81
        assert T1.world.width == 17
        assert str(T1.world.start_date) == "2022-02-22 00:00:00"
        assert T1.coordinate.x == 1
        assert T1.coordinate.y == 3
        assert T1.nutrient == 100

    def test_set_height(self):
        w1= World(81,17,"2022-02-22")
        p1= Point(1,3)
        T1 = Tree(p1,"2022-02-22",w1)
        T1.set_height(15)
        assert T1.get_height() == 15

class TestOak:

    def test_evolve(self):
        p1= Point(1,3)
        w1=World(81,17,"2022-02-22")
        O1 = Oak(p1,"2022-02-22",w1)
        O1.evolve()
        assert O1.height < MAX_HEIGHT
        O1.set_height(15)
        assert O1.get_height() == 15
        assert O1.width() == 0.12










