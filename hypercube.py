def found(l, x, y, arr):
    cross = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for check in cross:
        i, j = check
        try:
            if arr[x+i][y+j] == l:
                return (x+i, y+j, True)
        except IndexError:
            pass
    return (x+i, y+j, False)

def hypercube(grid):
    key = 'hypercube'
    grid = [[x.lower() for x in row] for row in grid]
    # find starting point
    for i, row in enumerate(grid):
        ok = True
        if 'h' in row:
            j = row.index('h')
            for letter in key[1:]:
                i, j, answ = found(letter, i, j, grid)
                if not answ: 
                    ok = False
                    break
            if ok == True:
                return True
    return False
    
print(hypercube([["H","a","t","s","E"],["h","Y","p","e","B"],["a","a","P","r","U"],["x","x","U","c","C"],["z","E","B","z","R"]]))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]) == True
    assert hypercube([
              ['H', 'a', 't', 's', 'E'],
              ['a', 'Y', 'p', 'u', 'B'],
              ['a', 'a', 'P', 'y', 'U'],
              ['x', 'x', 'x', 'E', 'C'],
              ['z', 'z', 'z', 'z', 'R']]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''


