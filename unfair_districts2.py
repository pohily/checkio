def unfair_districts(amount_of_people, grid):
    #from copy import deepcopy
    cross = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
    v = len(grid) - 1           #vertical border
    h = len(grid[0]) - 1        #horizontal border
    total_population = 0        #total population
    dis_number = 0              #number of districts

    grid_pop = []               #copy of grid with counted population of district
    for row in grid:
        grid_pop.append([])
        for district in row:
            grid_pop[-1].append(sum(district))
            total_population += sum(district)
            dis_number += 1
    if total_population % amount_of_people != 0:
        return []

    
    #find clasters with pop = aop
    
    used_districts = []         #districts used in finded zones
    current_zones = []          #list of current zones
    alt = []                    #alternative lookup
    
    while len(used_districts) < dis_number:
        
        current_population = 0      #population of current zone
        current_zone = []           #zone while its population less than AoP
        to_look = []                #list of available directions.    

        # find starting position
        for i, row in enumerate(grid_pop):
            ok = False
            for j, col in enumerate(row):
                if (i, j) not in used_districts:
                    ok = True
                    break
            if ok:
                break

        while current_population < amount_of_people:
            if not to_look:
                for c in cross:
                    x, y = c
                    if 0 <= x+i <= v and 0 <= y+j <= h:
                        if (x+i, y+j) not in used_districts and current_population + grid_pop[x+i][y+j] <= amount_of_people:
                            to_look.append((x+i, y+j))

            if to_look:
                i, j = to_look.pop(0)
                if current_population + grid_pop[i][j] <= amount_of_people and (i, j) not in current_zone:
                    current_population += grid_pop[i][j]
                    used_districts.append((i, j))
                    current_zone.append((i, j))
                else:
                    alt.append([current_zone[0]]+[(i, j)])  #not perfect
                    i, j = current_zone[-1]
        current_zones.append(current_zone)
    # check for winning candidate
    winners = []
    grid_zones = deepcopy(grid_pop) 
    mark = 64
    for i, zone in enumerate(current_zones):
        f = s = 0
        mark += 1
        
        for j, district in enumerate(zone):
            x, y = district
            grid_zones[x][y] = chr(mark)
            first, second = grid[x][y]
            if first > second:
                f += 1
            elif second > first:
                s += 1
        if f > s:
            winners.append('f')
        else:
            winners.append('s')

    return grid_zones
        
''' 
print(unfair_districts(5, [
        [[2, 1], [1, 1], [1, 2]],
        [[2, 1], [1, 1], [0, 2]]]))
'''

print(unfair_districts(9, [
        [[0, 3], [3, 3], [1, 1]],
        [[1, 2], [1, 0], [1, 1]],
        [[0, 3], [2, 1], [2, 2]]]))
'''

print(unfair_districts(8, [
        [[1, 1], [2, 0], [2, 0], [3, 3]],
        [[1, 1], [1, 2], [1, 1], [0, 3]],
        [[1, 1], [1, 1], [1, 2], [0, 3]],
        [[1, 1], [1, 1], [1, 1], [2, 0]]]))'''

