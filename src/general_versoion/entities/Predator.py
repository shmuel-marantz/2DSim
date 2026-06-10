from .MobileEntity import MobileEntity
from ..constants import PREDATOR_LIFESPAN
from .Herbivore import Herbivore

class Predator(MobileEntity):
    def __init__(self, x, y):
        super().__init__(x, y, PREDATOR_LIFESPAN, PREDATOR_LIFESPAN, [Herbivore])
        self.priority = 5
        self.icon = '🐺'

    def update(self, matrix):
        if self.handle_lifespan(matrix) == False:
            return
        if self.handle_movement(matrix) == 'ate':
            print(f'Alert: The predator in cell {self.x} {self.y} devoured a herbivore')