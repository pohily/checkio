coord = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
back = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L'}
checks_even = [[-1, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
checks_odd = [[-1, 0], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, -1]]
def decode_coord(point):
    return (int(point[1]) - 1, coord[point[0]])

def encode(point):
    return back[point[1]] + str(point[0]+1)

def supply_line(you, depots, enemies):
    def next_move(start, delta):
        todo = 0 # alternative path to look later
        # find next move toward end and return new position
        if delta[0] == 0 and delta[1] > 0:
            nearest = 1
            if (start[0]+1, start[1]+1) not in ZOC: 
                if start[1] % 2 == 0:
                    todo = (start[0]+1, start[1]+1)
                else:
                    todo = (start[0], start[1]-1)
        elif delta[0] == 0 and delta[1] < 0:
            nearest = 5
            if (start[0]+1, start[1]-1) not in ZOC: 
                if start[1] % 2 == 0:
                    todo = (start[0]+1, start[1]-1)
                else:
                    todo = (start[0], start[1]-1)
        elif delta[0] > 0 and delta[1] > 0:
            nearest = 2
        elif delta[0] > 0 and delta[1] < 0:
            nearest = 4
        elif delta[0] < 0 and delta[1] > 0:
            nearest = 0
            if (start[0], start[1]+1) not in ZOC: 
                if start[1] % 2 == 0:
                    todo = (start[0], start[1]+1)
                else:
                    todo = (start[0]-1, start[1]+1)
        elif delta[0] < 0 and delta[1] < 0:
            nearest = 5
            if (start[0]-1, start[1]) not in ZOC:
                todo = (start[0]+1, start[1])
        elif delta[0] < 0 and delta[1] == 0:
            nearest = 0
        elif delta[0] > 0 and delta[1] == 0:
            nearest = 3
        

        #check for ZOC if no - make move, if yes - find new direction
        for i in range(6):
            if start[1] % 2 == 0:
                row, col = checks_even[nearest]
            else:
                row, col = checks_odd[nearest]
            if (start[0] + row, start[1] + col) in ZOC or (start[0] + row, start[1] + col) in path:
                if todo:
                    start = todo
                    todo = 0
                    return (start[0], start[1]), todo
                else:
                    nearest = (nearest + 1) % 5
            else:
                if 0 <= row + start[0] <= 8 and 0 <= col + start[1] <= 11:
                    return (start[0]+row, start[1]+col), todo

    
    # find enemy ZOC
    ZOC = set()
    for enemy in enemies:
        row, col = decode_coord(enemy)
        if col % 2 == 0:
            for check in checks_even:
                if 0 <= row + check[0] <= 8 and 0 <= col + check[1] <= 11:
                    ZOC.add((row + check[0], col + check[1]))
        else:
            for check in checks_odd:
                if 0 <= row + check[0] <= 8 and 0 <= col + check[1] <= 11:
                    ZOC.add((row + check[0], col + check[1]))
            
    # just to see
    tmp = []
    for p in ZOC:
        tmp.append(encode(p))
    print('zoc', tmp)
    
    # check if depots in/out of ZOC
    tmp = []
    for depot in depots:
        row, col = decode_coord(depot)
        if (row, col) not in ZOC:
            tmp.append((row, col))
    depots = tmp

    # just to see
    tmp = []
    for p in depots:
        tmp.append(encode(p))
    print('depots', tmp)
    
    # find shortest way from you to every depot not in ZOC
    result = []
    alternative = []                # alternative path to look later
    for depot in depots:
        start = decode_coord(you)
        count = 0                   # step number
        visited = {start:count}     # visited places with step number
        path = [start]
        
        # delta is how far you must go in each coordinate
        delta = (depot[0] - start[0], depot[1] - start[1])
        while delta[0] or delta[1]:
            # make next move until delta != [0, 0] - means we reached depot
            alt = 0 # alternative path to look later
            start, alt = next_move(start, delta)
            path.append(start)
            count += 1
            visited[start] = count
            if (alt and alt not in visited) or (alt in visited and len(path) - 2 < visited[alt]):
                alternative.append(path + [alt])
            delta = (depot[0] - start[0], depot[1] - start[1])
        # just to see
        tmp = []
        for p in path:
            tmp.append(encode(p))
        path1 = tmp[:]    
        print('1', path1)
        result.append(len(path))
        
        # find alternative paths
        while alternative:
            path = alternative.pop()
            if path[-1] in visited and len(path) - 1 < visited[path[-1]] or path[-1] not in visited: 
                start = path[-1]
            else:
                continue
            delta = [depot[0] - start[0], depot[1] - start[1]]
            while delta[0] or delta[1]:
                # make next move until delta != [0, 0] - means we reached depot
                alt = 0 # alternative path to look later
                start, alt = next_move(start, delta)
                if start in visited and len(path) - 2 >= visited[start]:
                    continue
                path.append(start)
                count += 1
                visited[start] = count
                
                if (alt and alt not in visited) or (alt in visited and len(path) - 2 < visited[alt]):
                    alternative.append(path + [alt])
                delta = (depot[0] - start[0], depot[1] - start[1])
            # just to see
            tmp = []
            for p in path:
                tmp.append(encode(p))
            print('2', tmp)
            result.append(len(path))

    return min(result) - 1

print(supply_line("B4", {"F4"}, {"D4"}))
'''
if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("A3", {"A9", "F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')
'''
