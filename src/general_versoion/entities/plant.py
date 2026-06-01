import random
from ..constants import SPAWN_CHANCE, PLANT_LIFESPAN

def handle_growing_plants(matrix, i, j):
    if random.randint(1, 100) <= SPAWN_CHANCE * 100:
        matrix[i][j] = {'type': 'plant', 'lifespan': PLANT_LIFESPAN}
