import random
from .constants import *
from .entities.Empty import Empty
from .entities.Rock import Rock
from .entities.Entity import Entity
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
    embed_in_matrix(matrix, PLANT_AMOUNT, Plant)
    embed_in_matrix(matrix, HERBIVORE_AMOUNT, Herbivore)
    embed_in_matrix(matrix, PREDATOR_AMOUNT, Predator)
    embed_in_matrix(matrix, PERSON_AMOUNT, Person)
    return matrix

def play():
    matrix = create_matrix()
    for _ in range(STEPS):
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
        for i in matrix:
            for j in i:
                if isinstance(j, Empty):
                    j.update(matrix)
