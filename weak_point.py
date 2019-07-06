def find_min(arr):
    m = sum(arr[0])
    res = 0
    for i, v in enumerate(arr[1:]):
        j = sum(v)
        if m > j:
            res = i+1
            m = j
    return res
def weak_point(matrix):
    resH = find_min(matrix)
    matrix = list(zip(*matrix))
    resV = find_min(matrix)
    return resH, resV
print(weak_point([
                            [7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]]))    
"""

"""               



