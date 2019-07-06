def navigation(seaside):
    to_find = ['M', 'S', 'C', 'Y']
    coordinates = {}
    steps = 0
    for item in to_find:
        for index, row in enumerate(seaside):
            if item in row:
                coordinates[item] = (index, row.index(item))
    
    for item in to_find:
        if coordinates['Y'][0] == coordinates[item][0]:
            steps += abs(coordinates['Y'][1] - coordinates[item][1])
            continue
        elif coordinates['Y'][1] == coordinates[item][1]:
            steps += abs(coordinates['Y'][0] - coordinates[item][0])
            continue
        else:
            v = abs(coordinates['Y'][0] - coordinates[item][0])
            h = abs(coordinates['Y'][1] - coordinates[item][1])
            if v <= h:
                if coordinates['Y'][1] < coordinates[item][1]:
                    ### Y lefter
                    steps += v + abs((coordinates['Y'][1] + v) - coordinates[item][1])
                else:
                    ### Y righter
                    steps += v + abs((coordinates['Y'][1] - v) - coordinates[item][1])
            else:
                ### Y higher
                if coordinates['Y'][0] < coordinates[item][0]:
                    steps += h + abs((coordinates['Y'][0] + h) - coordinates[item][0])
                else:
                ### Y lower
                    steps += h + abs((coordinates['Y'][0] - h) - coordinates[item][0])
    
    return steps
    
print(navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]))


