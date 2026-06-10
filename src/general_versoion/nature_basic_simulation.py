import random
from .constants import *
from .entities.Empty import Empty
from .entities.Rock import Rock
from .entities.Entity import Entity
from .entities.MobileEntity import MobileEntity
from .entities.Plant import Plant
from .entities.Herbivore import Herbivore
from .entities.Predator import Predator
from .entities.Person import Person

def embed_in_matrix(matrix, amount, entity):
    for _ in range(amount):
        flag = False
        while flag == False:
            y = random.randint(0, len(matrix) - 1)
            x = random.randint(0, len(matrix[0]) - 1)
            if isinstance(matrix[y][x], Empty):
                matrix[y][x] = entity(x, y)
                flag = True

def create_matrix():
    matrix = []
    for i in range(GRID_HEIGHT):
        row = []
        for j in range(GRID_WIDTH):
            row.append(Empty(j, i))
        matrix.append(row)
    embed_in_matrix(matrix, ROCK_AMOUNT, Rock)
    embed_in_matrix(matrix, HERBIVORE_AMOUNT, Herbivore)
    embed_in_matrix(matrix, PREDATOR_AMOUNT, Predator)
    embed_in_matrix(matrix, PERSON_AMOUNT, Person)
    return matrix

def play():
    matrix = create_matrix()
    alert_already_was = False
    for _ in range(STEPS + 1):
        count_plants = 0
        mobile_entity_exists = False
        for i in matrix:
            for j in i:
                if isinstance(j, MobileEntity):
                    mobile_entity_exists = True
                if isinstance(j, Empty):
                    j.update(matrix)
                if type(matrix[j.y][j.x]) is Plant:
                    count_plants += 1
        if mobile_entity_exists == False and not alert_already_was:
            print('Alert: There are no more mobile entities alive')
            alert_already_was = True
        if GRID_HEIGHT * GRID_WIDTH * PLANT_ALERT_THRESHOLD < count_plants:
            print(f'Alert: the number of plants exceeded {PLANT_ALERT_THRESHOLD * 100}% of the grid space')
        for i in matrix: 
            for j in i:
                print(j.icon, end="")
            print("")
        print('===========================================')
        entities = []
        for i in matrix:
            for j in i:
                if isinstance(j, Entity):
                    entities.append(j)
        entities.sort(key=lambda e: e.priority)
        for e in entities:
            if e.is_alive:
                e.update(matrix)
