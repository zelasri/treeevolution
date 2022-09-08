"""
Module which enables to simulate a world
"""
from datetime import date

from treevolution import World
from treevolution.base import Point
from treevolution.models.trees import Oak

def main():
    """
    Main function which simulates the world
    """
    w_world, h_world = 200, 200

    current_date = date.today()
    world = World(current_date, w_world, h_world)

    # create trees
    for _ in range(5):
        point = Point.random(w_world, h_world)
        tree = Oak(point, current_date, world)

        world.add_tree(tree)

    # simulate 1000 days    
    for _ in range(1000):
        
        day, _, trees, seeds = world.step()

        if len(trees) > 0:
            print(f'{day}: (trees: {len(trees)}, seeds: {len(seeds)})')


if __name__ == "__main__":
    main()
