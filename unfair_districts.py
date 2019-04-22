def unfair_districts(amount_of_people, grid):
    grid1 = grid[:]
    for i, row in enumerate(grid):
        for j, district in enumerate(row):
            if district[0] > district[1]:
                grid1[i][j] = (1, sum(district))
            elif district[1] > district[0]:
                grid1[i][j] = (2, sum(district))
            else:
                grid1[i][j] = (0, sum(district))
    return grid1
print(unfair_districts(5, [
        [[2, 1], [1, 1], [1, 2]],
        [[2, 1], [1, 1], [0, 2]]]))
print(unfair_districts(9, [
        [[0, 3], [3, 3], [1, 1]],
        [[1, 2], [1, 0], [1, 1]],
        [[0, 3], [2, 1], [2, 2]]]))
print(unfair_districts(8, [
        [[1, 1], [2, 0], [2, 0], [3, 3]],
        [[1, 1], [1, 2], [1, 1], [0, 3]],
        [[1, 1], [1, 1], [1, 2], [0, 3]],
        [[1, 1], [1, 1], [1, 1], [2, 0]]]))
"""

""" 
