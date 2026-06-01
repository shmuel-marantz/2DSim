import random, copy

def get_neighbors(matrix, i, j):
    neighbors = []
    if j != 0:
        neighbors.append(matrix[i][j - 1])
        if i != 0:
            neighbors.append(matrix[i - 1][j - 1])
    if i != 0:
        neighbors.append(matrix[i - 1][j])
        if j != len(matrix[0]) - 1:
            neighbors.append(matrix[i - 1][j + 1])
    if j != len(matrix[0]) - 1:
        neighbors.append(matrix[i][j + 1])
        if i != len(matrix) - 1:
            neighbors.append(matrix[i + 1][j + 1])
    if i != len(matrix) - 1:
        neighbors.append(matrix[i + 1][j])
        if j != 0:
            neighbors.append(matrix[i + 1][j - 1])
    return neighbors

def make_turn(matrix):
    mtx = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            neighbors = get_neighbors(matrix, i, j)
            count_0 = neighbors.count('0')
            if count_0 > 3 or count_0 < 2:
                mtx[i][j] = "."
            if count_0 == 3:
                mtx[i][j] = '0'
    return mtx

def get_matrix(file_name):
    matrix = []
    with open(file_name) as f:
        for line in f:
            row = list(line.strip())
            matrix.append(row)
    return matrix

def choose_seed():
    print("""Choose a seed:
1. Circle
2. Lattice
3. Snake
4. Create seed""")
    num = input()
    while num not in ['1', '2', '3', '4']:
        num = input('Choose between 1 and 4\n')
    num = int(num)
    if num == 1:
        seed = "circle"
    if num == 2:
        seed = "lattice"
    if num == 3:
        seed = "snake"
    if num == 4:
        seed = "create"
    return seed

def create_matrix():

    mtx_length = input('Choose length. Enter a number between 10 end 40\n')
    while not mtx_length.isdigit() or not 41 > int(mtx_length) > 9:
        mtx_length = input('Choose length. Enter a positive integer between 10 end 40\n')
    mtx_length = int(mtx_length)

    mtx_width = input('Choose width. Enter a number between 10 end 40\n')
    while not mtx_width.isdigit() or not 41 > int(mtx_width) > 9:
        mtx_width = input('Choose width. Enter a positive integer between 10 end 40\n')
    mtx_width = int(mtx_width)

    chance_for_0 = input('Choose a number between 0 and 100 for chance for a live cell:\n')
    while not chance_for_0.isdigit() or int(chance_for_0) > 100:
        chance_for_0 = input('Choose a number between 0 and 100 for chance for 0:\n')
    chance_for_0 = int(chance_for_0)

    matrix = []
    for i in range(mtx_length):
        row = []
        for j in range(mtx_width):
            if random.randint(0, 100) > chance_for_0:
                row.append('.')
            else:
                row.append('0')
        matrix.append(row)
    return matrix
