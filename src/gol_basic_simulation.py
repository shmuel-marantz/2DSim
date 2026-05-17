import time, pygame
from .utils import *

def play ():

    seed = choose_seed()
    if seed == 'create':
        matrix = create_matrix()
    else:
        matrix = get_matrix(f'seeds/{seed}_seed.txt')

    num = input('Enter a number for turns:\n')
    while not num.isdigit():
        num = input('Enter a number for turns:\n')
    num = int(num)

    pygame.init()
    screen = pygame.display.set_mode((len(matrix[0])*13, len(matrix)*13))
    BLUE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TILE_SIZE = 13
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        
        for row_index, row in enumerate(matrix):
            for col_index, value in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                if value == '0':
                    pygame.draw.rect(screen, BLUE, rect)
                    
        pygame.display.flip() 

        if num > 0:
            matrix = make_turn(matrix)
            num -= 1    
            time.sleep(0.2)
        
    pygame.quit()
