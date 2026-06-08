from .Entity import Entity
from ..constants import PLANT_LIFESPAN

class Plant(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, PLANT_LIFESPAN)
        self.priority = 15
        self.icon = '🌿'
    
    def update(self, matrix):
        self.handle_lifespan(matrix)