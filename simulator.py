from interface import ITerrain
import random

class Simulator:

    def __init__(self,terrain:ITerrain):
        self.terrain = terrain
        self.steps = 0

    def step(self):
        new_root = []

        for root in self.terrain.get_root():
            x, y = root.get_position()
            spaces = self.terrain.free_spaces(x,y)
            if spaces:
                dest = random.choice(spaces)
                new_root.append(dest)

        for x,y in new_root:
            self.terrain.add_root(x,y)
        
        self.steps += 1
        return len(new_root) > 0