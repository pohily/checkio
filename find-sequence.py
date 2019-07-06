def check(m):
    m_str = []
    for row in m:
        tmp = ''
        for i in row:
            tmp += str(i)
        m_str.append(tmp)
    for row in m_str:
        for i in range(10):
            if str(i)*4 in row:
                print(str(i)*4)
                return True
    return False

def checkio(matrix):
    if check(matrix) == True:
        return True
    
    diag = []
    for i in range(len(matrix) - 4+1):
        t1 = []
        t2 = []
        t3 = []
        t4 = []
        for j in range(len(matrix) - i):
            t1.append(matrix[j][j+i])
            t2.append(matrix[j+i][j])
            t3.append(matrix[j][len(matrix) - (j+i) - 1])
            t4.append(matrix[j+i][len(matrix) - j - 1])
        diag.append(t1)
        diag.append(t2)
        diag.append(t3)
        diag.append(t4)
    print(diag)
    if check(diag) == True:
        return True

    matrix = list(zip(*matrix))
    if check(matrix) == True:
        return True
    return False


print(checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]))
"""

    """


