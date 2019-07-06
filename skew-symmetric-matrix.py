def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -(matrix[j][i]):
                return False
    return True
        
print(checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]))
"""

"""               



