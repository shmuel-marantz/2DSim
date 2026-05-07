def ff():
    matrix = [["." for _ in range(20)] for _ in range(11)]
    matrix[3][7], matrix[3][9], matrix[3][11] = 0, 0, 0
    matrix[7][7], matrix[7][9], matrix[7][11] = 0, 0, 0
    matrix[4][6], matrix[4][12] = 0, 0
    matrix[6][6], matrix[6][12] = 0, 0
    matrix[5][5], matrix[5][7], matrix[5][11], matrix[5][13] = 0, 0, 0, 0
    return matrix


def f():
    matrix = ff()
    mtx = ff()
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


m1 = f()

m2 = ff()


def fff(m):
    for i in m:
        for j in i:
            print(j, end="")
        print("")
# print('----------------------------------')
fff(m2)
while True:
    matrix = ff()
    mtx = ff()
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