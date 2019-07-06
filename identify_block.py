def identify_block(numbers):
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *

    """
    ancor = min(numbers)
    if ancor + 4 in numbers and ancor + 8 in numbers and ancor + 12 in numbers:
        return 'I'
    elif ancor + 1 in numbers and ancor + 2 in numbers and ancor + 3 in numbers:
        return 'I'
    elif ancor not in [1, 5] and ancor + 4 in numbers and ancor + 7 in numbers and ancor + 8 in numbers:
        return 'J'
    elif ancor not in [3, 4, 7, 8] and ancor + 4 in numbers and ancor + 5 in numbers and ancor + 6 in numbers:
        return 'J'
    elif ancor not in [4, 8] and ancor + 1 in numbers and ancor + 4 in numbers and ancor + 8 in numbers:
        return 'J'
    elif ancor not in [3, 4, 7, 8] and ancor + 1 in numbers and ancor + 2 in numbers and ancor + 6 in numbers:
        return 'J'
    elif ancor not in [3, 4, 7] and ancor + 4 in numbers and ancor + 8 in numbers and ancor + 9 in numbers:
        return 'L'
    elif ancor not in [1, 2, 5, 6, 9, 10] and ancor + 4 in numbers and ancor + 2 in numbers and ancor + 3 in numbers:
        return 'L'
    elif ancor != 4 and ancor + 1 in numbers and ancor + 5 in numbers and ancor + 9 in numbers:
        return 'L'
    elif ancor + 1 in numbers and ancor + 2 in numbers and ancor + 4 in numbers:
        return 'L'
    elif ancor + 1 in numbers and ancor + 4 in numbers and ancor + 5 in numbers:
        return 'O'
    elif ancor not in [4, 8, 12] and ancor + 1 in numbers and ancor + 4 in numbers and ancor + 3 in numbers:
        return 'S'
    elif ancor != 4 and ancor + 4 in numbers and ancor + 5 in numbers and ancor + 9 in numbers:
        return 'S'
    elif ancor not in [3, 4, 7, 8] and ancor + 1 in numbers and ancor + 5 in numbers and ancor + 6 in numbers:
        return 'Z'
    elif ancor not in [1, 5, 9] and ancor + 3 in numbers and ancor + 4 in numbers and ancor + 7 in numbers:
        return 'Z'
    elif ancor not in [3, 4, 7, 8, 11] and ancor + 1 in numbers and ancor + 2 in numbers and ancor + 5 in numbers:
        return 'T'
    elif ancor not in [1, 5] and ancor + 4 in numbers and ancor + 8 in numbers and ancor + 3 in numbers:
        return 'T'
    elif ancor not in [1, 5, 9, 4, 8] and ancor + 4 in numbers and ancor + 5 in numbers and ancor + 3 in numbers:
        return 'T'
    elif ancor not in [4, 8] and ancor + 4 in numbers and ancor + 5 in numbers and ancor + 8 in numbers:
        return 'T'
    return None

print(identify_block({10, 13, 14, 15}))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')




import numpy as np
from itertools import product

BLOCKS = {
    'T': {(0, 0), (0, 1), (0, 2), (1, 1)},
    'I': {(0, 0), (1, 0), (2, 0), (3, 0)},
    'O': {(0, 0), (0, 1), (1, 0), (1, 1)},
    'L': {(0, 0), (1, 0), (2, 0), (2, 1)},
    'J': {(0, 1), (1, 1), (2, 0), (2, 1)},
    'S': {(0, 1), (0, 2), (1, 0), (1, 1)},
    'Z': {(0, 0), (0, 1), (1, 1), (1, 2)},
}


def identify_block(tile):
    grid = np.arange(1, 17).reshape((4, 4))
    for (name, coords), r in product(BLOCKS.items(), range(4)):
        grid = np.rot90(grid)
        tile_coord = {(x, y) for x, y in product(range(4), repeat=2) if grid[x, y] in tile}
        if len(set((b[0] - t[0], b[1] - t[1]) for b, t in zip(sorted(coords), sorted(tile_coord)))) == 1:
            return name
'''

