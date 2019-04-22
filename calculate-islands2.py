def checkio(land_map):
    v = len(land_map)
    h = len(land_map[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = []
    islands = []
    while len(visited) < h*v:
        #find starting position  - first 1
        for x in range(v):
            found = False
            for y in range(h):
                if (x, y) not in visited and land_map[x][y] == 0:
                    visited.append((x, y))
                elif (x, y) not in visited and land_map[x][y] == 1:
                    found = True
                    visited.append((x, y))
                    islands.append([(x, y)])
                    break
            if found:
                break
        
        #find all 1's connected
        for point in islands[-1]:
            x, y = point
            for direction in directions:
                i, j = direction
                if 0 <= x + i < v and 0 <= y + j < h:
                    if (x+i, y+j) not in visited and land_map[x+i][y+j] == 1:
                        visited.append((x+i, y+j))
                        islands[-1].append((x+i, y+j))
                    elif (x+i, y+j) not in visited and land_map[x+i][y+j] == 0:
                        visited.append((x+i, y+j))
    return sorted([len(i) for i in islands])
   

if __name__ == '__main__':
    
    print(checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]))
    
    
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    



