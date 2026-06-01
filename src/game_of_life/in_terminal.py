import time, os
from .utils import *

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="")
        print("")

def play():

    seed = choose_seed()
    if seed == 'create':
        matrix = create_matrix()
    else:
        matrix = get_matrix(f'seeds/{seed}_seed.txt')

    num = input('Enter a number for turns:\n')
    while not num.isdigit():
        num = input('Enter a number for turns:\n')
    num = int(num)

    while num != -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_matrix(matrix)
        matrix = make_turn(matrix)
        time.sleep(0.2)
        num -= 1
