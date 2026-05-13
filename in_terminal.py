import copy, time, os

def create_matrix():
    matrix = [["." for _ in range(20)] for _ in range(11)]
    matrix[3][7], matrix[3][9], matrix[3][11] = 0, 0, 0
    matrix[7][7], matrix[7][9], matrix[7][11] = 0, 0, 0
    matrix[4][6], matrix[4][12] = 0, 0
    matrix[6][6], matrix[6][12] = 0, 0
    matrix[5][5], matrix[5][7], matrix[5][11], matrix[5][13] = 0, 0, 0, 0
    return matrix

def make_turn(matrix):
    mtx = copy.deepcopy(matrix)
    for i in range(11):
        for j in range(20):
            count = 0
            if j != 0:
                if matrix[i][j - 1] == 0:
                    count += 1
                if i != 0:
                    if matrix[i - 1][j - 1] == 0:
                        count += 1
            if i != 0:
                if matrix[i - 1][j] == 0:
                    count += 1
                if j != 19:
                    if matrix[i - 1][j + 1] == 0:
                        count += 1
            if j != 19:
                if matrix[i][j + 1] == 0:
                    count += 1
                if i != 10:
                    if matrix[i + 1][j + 1] == 0:
                        count += 1
            if i != 10:
                if matrix[i + 1][j] == 0:
                    count += 1
                if j != 0:
                    if matrix[i + 1][j - 1] == 0:
                        count += 1
            if count > 3 or count < 2:
                mtx[i][j] = "."
            if count == 3:
                mtx[i][j] = 0
    return mtx

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="")
        print("")

def play():
    
    num = int(input('enter a number:\n'))
    matrix = create_matrix()
    while num != -1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_matrix(matrix)
        matrix = make_turn(matrix)
        time.sleep(0.2)
        num -= 1

ply()