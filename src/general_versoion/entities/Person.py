from .MobileEntity import MobileEntity
from ..constants import PERSON_LIFESPAN
from .Plant import Plant
from .Herbivore import Herbivore
from .Predator import Predator

class Person(MobileEntity):
    def __init__(self, x, y):
        super().__init__(x, y, PERSON_LIFESPAN, PERSON_LIFESPAN, [Plant, Herbivore, Predator])
        self.priority = 3
        self.icon = '🧑'

    def update(self, matrix):
        if self.handle_lifespan(matrix) == False:
            return
        self.handle_movement(matrix)