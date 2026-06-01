from src.game_of_life.in_terminal import play as play1
from src.game_of_life.gol_basic_simulation import play as play2
from src.general_versoion.nature_basic_simulation import play as play3

def play():
    choice = input('''Choose:
1. Game of Life in terminal
2. Game of Life in pygame
3. General version
''')
    while choice not in ['1', '2', '3']:
        choice = input("Choose 1, 2 or 3")
    if choice == '1':
        play1()
    if choice == '2':
        play2()
    if choice == '3':
        play3()

play()