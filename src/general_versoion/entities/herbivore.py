from .utils import get_neighbors, handle_animal_movement
from ..constants import HERBIVORE_LIFESPAN, PREVENTS_REPRODUCTION

def handle_herbivore_actions(matrix, i, j, entity, switch):
    if entity['switch'] == switch:
        return 
    entity['switch'] = switch
    close_neighbors = get_neighbors(matrix, i, j)
    if entity['prevents reproduction'] == 0:
        for _, neighbor in close_neighbors.items():
            if neighbor['type'] == 'herbivore' and neighbor['prevents reproduction'] == 0 and neighbor['switch'] != switch:
                for location1, neighbor1 in close_neighbors.items():
                    if neighbor1['type'] == 'empty':
                        xy = {'upper': [i - 1, j], 'left': [i, j - 1], 'right': [i, j + 1], 'lower': [i + 1, j]}
                        matrix[xy[location1][0]][xy[location1][1]] = {'switch': switch, "type": "herbivore", "lifespan": HERBIVORE_LIFESPAN, "prevents reproduction": 0}
                        entity['prevents reproduction'] = PREVENTS_REPRODUCTION
                        neighbor['prevents reproduction'] = PREVENTS_REPRODUCTION
                        neighbor['switch'] = switch
                        return
                entity['switch'] == 'There is no room for reproduction'
                break    
    handle_animal_movement(matrix, i, j, entity, 'plant', HERBIVORE_LIFESPAN)