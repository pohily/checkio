def g_key(grid, path):
    #replace this for solution
    return 0


print(g_key([
                  [1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9))
'''
"""
A lot of code, and I think is not particulary fast but i think is 'clearish'.
Any improvements, suggestions  are really appreciated. This is the first problem
I have solved in Checkio that is really chalenging for me and I am eagger to 
learn what more knowledgeable people can teach me.
"""
directions = ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))


def g_key(grid, path):
    """
    gets the path len equal to PATH with the bigest sum given a matrix of
    integers GRID
    """
    n = len(grid) * len(grid[0])
    if n == path:
        return sum([item for line in grid for item in line])

    results = []

    ord_grid = [(i, x, y) for y, l in enumerate(grid) for x, i in enumerate(l)]
    start, ord_grid, end = ord_grid[0], ord_grid[1:-1], ord_grid[-1]
    ord_grid.sort(key=lambda x: x[0], reverse=True)
    posible_path = get_path(len(ord_grid), path - 2)

    c = factorial(n - 2) // (factorial(path - 2) * factorial(n - path))

    for i in range(c):
        p = [ord_grid[x] for x in next(posible_path)] + [start, end]
        results.append((p, sum([x[0] for x in p])))

    for result in sorted(results, key=lambda x: x[1], reverse=True):
        p = [(x, y) for v, x, y in result[0]]
        if walk_path(0, 0, p):
            return result[1]


def factorial(n):
    #good old recursive factorial
    return 1 if n == 0 else n * factorial(n - 1)


def get_path(total, path):
    """
    Returns a list of indexes with len equals PATH trying to maximaze the sum
    of them this helps to order the posible paths a little faster
    """
    p_path = list(range(path)) + [total + 1]
    yield(p_path[:-1])
    while p_path[0] <= total - path:
        for x in range(0, len(p_path)):
            p_path[-x - 1] = p_path[-x - 1] + (p_path[-x] + x > total + 1)
        for n in range(1, len(p_path) - 1):
            p_path[n] = p_path[n] if p_path[n] < n + total + 1  - path else p_path[n - 1] + 1  
        yield(p_path[:-1])


def walk_path(ox, oy, path):
    """
    Gets the posible moves from ox, oy in path and then calls itself for each
    posible move then if all points in the path were visited returns true.
    """
    posible_moves = [(x, y) for x, y in path if (ox - x, oy - y) in directions]
    if path == []:
        return True
    for px, py in posible_moves:
        if walk_path(px, py, list(set(path) - set([(px, py), (ox, oy)]))):
            return True
'''
