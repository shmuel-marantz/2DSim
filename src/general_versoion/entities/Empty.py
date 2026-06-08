import random
from ..constants import SPAWN_CHANCE

class Empty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.icon = '⬛'
    def update(self, matrix):
        if random.randint(1, 100) <= SPAWN_CHANCE * 100:
            from .Plant import Plant
            matrix[self.y][self.x] = Plant(self.x, self.y)