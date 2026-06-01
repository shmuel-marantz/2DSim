from .utils import handle_animal_movement
from ..constants import PREDATOR_LIFESPAN

def handle_predator_actions(matrix, i, j, entity, switch):
    if entity['switch'] == switch:
        return 
    entity['switch'] = switch
    handle_animal_movement(matrix, i, j, entity, 'herbivore', PREDATOR_LIFESPAN)