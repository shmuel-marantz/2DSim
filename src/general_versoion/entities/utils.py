import random

def get_neighbors(matrix, i, j):
    close_neighbors = {}
    if i != 0:
        close_neighbors['upper'] = matrix[i - 1][j]
    if j != 0:
        close_neighbors['left'] = matrix[i][j - 1]
    if j != len(matrix[0]) - 1:
        close_neighbors['right'] = matrix[i][j + 1]
    if i != len(matrix) - 1:
        close_neighbors['lower'] = matrix[i + 1][j]
    return close_neighbors

def handle_animal_movement(matrix, i, j, entity, goal, lifespan):
    xy = {'upper': [i - 1, j], 'left': [i, j - 1], 'right': [i, j + 1], 'lower': [i + 1, j]}
    close_neighbors = get_neighbors(matrix, i, j)
    for location, neighbor in close_neighbors.items():
        if neighbor['type'] == goal:
            entity['lifespan'] = lifespan
            matrix[i][j] = {'type': "empty"}
            matrix[xy[location][0]][xy[location][1]] = entity
            return
    for location, neighbor in close_neighbors.items():
        if neighbor['type'] in ['plant', 'empty']:
            neighbors_neighbor = get_neighbors(matrix, xy[location][0], xy[location][1])
            for _, neighbor1 in neighbors_neighbor.items():
                if neighbor1['type'] == goal:
                    matrix[i][j] = {'type': "empty"}
                    matrix[xy[location][0]][xy[location][1]] = entity
                    return
    potential_targets = []
    for location, neighbor in close_neighbors.items():
        if neighbor['type'] == 'empty':
            potential_targets.append(location)
    if len(potential_targets) == 0:
        return
    random_target = potential_targets[random.randint(0, len(potential_targets) - 1)]
    matrix[i][j] = {'type': "empty"}
    matrix[xy[random_target][0]][xy[random_target][1]] = entity
