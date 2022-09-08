"""
Module which simulates the world with interface
"""
from datetime import date
import random

import tkinter as tk

from treevolution import World
from treevolution.context import Season
from treevolution.base import Point
from treevolution.models.trees import Oak
from treevolution.models import TreeState

# some world parameters
SCALE_BY = 20
W_WORLD, H_WORLD = 100, 100

def scale(x_value):
    """
    Enable to scale a value by constant and returns it
    """
    return SCALE_BY * x_value

# Create an instance of tkinter frame
root = tk.Tk()
# Define the geometry of root
root.geometry(f"{scale(W_WORLD)}x{scale(H_WORLD)}")
root.title("Treevolution")

# does not work..
#root.tk.call('tk', 'scaling', 2.0)

NDAYS = 0
SEED_RADIUS = scale(0.2)

def main():
    """
    Simulate the world with a Tkinter interface
    """

    current_date = date.today()
    random.seed(42)

    # 1. create world context
    world = World(current_date, W_WORLD, H_WORLD)

    # create a certain number of trees
    for _ in range(20):
        point = Point.random(W_WORLD, H_WORLD)
        tree = Oak(point, current_date, world)
        world.add_tree(tree)

    #Create a canvas object
    canvas = tk.Canvas(root, width=scale(W_WORLD), height=scale(H_WORLD))
    canvas.pack()

    label_text = tk.StringVar()
    label_text.set("Welcome to this simulation!")
    label = tk.Label(canvas, textvariable=label_text, font=("Helvetica", 16))
    label.place(x=2, y=10)

    # need to create inner update function with the whole contexte
    def update():

        # known issue, but needed in order to update the variable 
        # in tkinter context
        # pylint: disable=global-statement
        global NDAYS
        # pylint: enable=global-statement
        
        if NDAYS > 10000:
            return

        day, _, trees, seeds = world.step()

        canvas.delete("all")

        for tree in trees:

            x_coord, y_coord = scale(tree.coordinate.x), scale(tree.coordinate.y)
            radius = scale(tree.radius)

            # yellow for humus state
            color = 'green' if tree.state == TreeState.TREE else 'yellow'

            canvas.create_oval(x_coord - radius, y_coord - radius, x_coord + radius, 
                            y_coord + radius, width=3, fill=color)
                

        for seed in seeds:

            x_coord, y_coord = scale(seed.coordinate.x), scale(seed.coordinate.y)

            canvas.create_oval(x_coord - SEED_RADIUS, y_coord - SEED_RADIUS, \
                x_coord + SEED_RADIUS, y_coord + SEED_RADIUS, width=3, fill="red")

        print(f'{day}: (trees: {len(trees)}, seeds: {len(seeds)})')

        season = Season.get(day)

        label_text.set(f'{day}: (trees: {len(trees)}, '\
                f'seeds: {len(seeds)}) [{Season.to_str(season)}]')

        NDAYS += 1
        root.after(10, update) # call update() after 0.1 second

    update() # start the periodic update

    root.mainloop()


if __name__ == "__main__":
    main()
