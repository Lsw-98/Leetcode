def setZeroes(matrix):
    index = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                index.append([i, j])
    for k in range(len(index)):
        for i in range(len(matrix)):
            matrix[i][index[k][1]] = 0
        for j in range(len(matrix[0])):
            matrix[index[k][0]][j] = 0

