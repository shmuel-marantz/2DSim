from src.in_terminal import play as play1
from src.gol_basic_simulation import play as play2


def play():
    choice = input("choose: 1. terminal. 2. pygame\n")
    while choice not in ['1', '2']:
        choice = input("choose 1 or 2")
    if choice == '1':
        play1()
    else:
        play2()

play()