from typing import List

def checkio(land_map: List[List[int]]) -> List[int]:
    land, count = [], 0
    for i in range(len(land_map)):                          #find all the land
        for j in range(len(land_map[0])):
            if land_map[i][j] == 1:
                if not (i, j) in land:
                    land.append((i, j))
    
    islands = [[]]
    for l in land:
        near = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0<= l[0] + i <= len(land_map)-1 and 0<= l[1] + j <= len(land_map[0]) - 1:
                     if land_map[l[0] + i][l[1] + j] == 1:
                        if land_map[l[0] + i][l[1] + j] not in islands[count] and land_map[l[0]][l[1]] == 1:
                            if i!=0 or j!=0:
                                near = True
                                islands[count].append((l[0] + i, l[1] + j))
                        elif land_map[l[0] + i][l[1] + j] not in islands[count] and land_map[l[0]][l[1]] == 0:
                            if i!=0 or j!=0:
                                count += 1
                                islands[count].append((l[0] + i, l[1] + j))
                            
        if near == True and land_map[l[0]][l[1]] == 1:
            islands[count].append(l)
        elif near == False and land_map[l[0]][l[1]] == 1:
            count += 1
            islands.append([])
            islands[count].append(l)
    result = []
    for i in range(len(islands)):
        islands[i] = sorted(set(islands[i]))
        result.append(len(islands[i]))
    print(islands)
    return sorted(result)



print(checkio([
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]]))
                    



