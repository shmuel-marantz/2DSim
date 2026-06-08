def get_neighbors(matrix, i, j):
        close_neighbors = []
        if i != 0:
            close_neighbors.append(matrix[i - 1][j])
        if j != 0:
            close_neighbors.append(matrix[i][j - 1])
        if j != len(matrix[0]) - 1:
            close_neighbors.append(matrix[i][j + 1])
        if i != len(matrix) - 1:
            close_neighbors.append(matrix[i + 1][j])
        return close_neighbors
