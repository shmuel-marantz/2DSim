from .MobileEntity import MobileEntity
from .Plant import Plant
from ..constants import HERBIVORE_LIFESPAN, PREVENTS_REPRODUCTION

class Herbivore(MobileEntity):
    def __init__(self, x, y):
        super().__init__(x, y, HERBIVORE_LIFESPAN, HERBIVORE_LIFESPAN, [Plant])
        self.max_prevents_reproduction = PREVENTS_REPRODUCTION
        self.current_prevents_reproduction = 0
        self.priority = 10
        self.icon = '🐐'

    def update(self, matrix):
        if self.handle_lifespan(matrix) == False:
            return
        if self.reproduce(matrix) == True:
            return
        self.handle_movement(matrix)