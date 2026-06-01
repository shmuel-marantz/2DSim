import random

from .constants import *
from .entities.plant import handle_growing_plants
from .entities.herbivore import handle_herbivore_actions
from .entities.predator import handle_predator_actions

icons = {'empty': '⬛', 'rock': '🔴', 'plant': '🌿', 'herbivore': '🐐', 'predator': '🐺'}

def get_random_cell(matrix):
    return random.randint(0, len(matrix) - 1), random.randint(0, len(matrix[0]) - 1)

def make_turn(matrix, switch):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            entity = matrix[i][j]
            if entity['type'] in ['rock', 'empty']:
                continue
            if entity.get('switch') != switch:
                if entity.get('lifespan') == 0:
                    matrix[i][j] = {'type': 'empty'}
                    continue
                else:
                    entity['lifespan'] -= 1
            if entity['type'] == 'predator':
                handle_predator_actions(matrix, i, j, entity, switch)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            entity = matrix[i][j]
            if entity['type'] == 'herbivore':
                handle_herbivore_actions(matrix, i, j, entity, switch)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            entity = matrix[i][j]
            if entity['type'] == 'empty':
                handle_growing_plants(matrix, i, j)
            
def play():
    matrix = []
    for _ in range(GRID_HEIGHT):
        row = []
        for _ in range(GRID_WIDTH):
            row.append({'type': "empty"})
        matrix.append(row)
    for _ in range(ROCK_AMOUNT):
        flag = False
        while flag == False:
            y = get_random_cell(matrix)[0]
            x = get_random_cell(matrix)[1]
            if matrix[y][x]['type'] == 'empty':
                matrix[y][x] = {'type': 'rock'}
                flag = True
    for _ in range(PLANT_AMOUNT):
        flag = False
        while flag == False:
            y = get_random_cell(matrix)[0]
            x = get_random_cell(matrix)[1]
            if matrix[y][x]['type'] == 'empty':
                matrix[y][x] = {'type': 'plant', 'lifespan': PLANT_LIFESPAN}
                flag = True
    for _ in range(HERBIVORE_AMOUNT):
        flag = False
        while flag == False:
            y = get_random_cell(matrix)[0]
            x = get_random_cell(matrix)[1]
            if matrix[y][x]['type'] == 'empty':
                matrix[y][x] = { 'switch': 'even', "type": "herbivore", "lifespan": HERBIVORE_LIFESPAN, "prevents reproduction": 0}
                flag = True
    for _ in range(PREDATOR_AMOUNT):
        flag = False
        while flag == False:
            y = get_random_cell(matrix)[0]
            x = get_random_cell(matrix)[1]
            if matrix[y][x]['type'] == 'empty':
                matrix[y][x] = { 'switch': 'even', "type": "predator", "lifespan": PREDATOR_LIFESPAN}
                flag = True
    switch = 'even'
    for _ in range(15):
        for i in matrix:
            for j in i:
                print(icons[j['type']], end="")
            print("")
        print('===========================================')
        if switch == 'even':
            switch = 'odd'
        else:
            switch = 'even'
        make_turn(matrix, switch)
