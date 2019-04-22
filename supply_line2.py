coord = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
back = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L'}
checks_odd = [[-1, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
checks_even = [[-1, 0], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, -1]]


def decode_coord(point):
    return (int(point[1]) - 1, coord[point[0]])

def encode(point):
    return back[point[1]] + str(point[0]+1)

def supply_line(you, depots, enemies):
    #dup of our map
    tmp_map = [['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '']]          
        
    # find enemy ZOC
    ZOC = set()
    for enemy in enemies:
        row, col = decode_coord(enemy)
        ZOC.add((row, col))
        tmp_map[row][col] = 'z'
        if col % 2 == 0:
            checks = checks_even
        else:
            checks = checks_odd
        for check in checks:
            if 0 <= row + check[0] <= 8 and 0 <= col + check[1] <= 11:
                ZOC.add((row + check[0], col + check[1]))
                tmp_map[row + check[0]][col + check[1]] = 'z'
    # just to see
    tmp = []
    for p in ZOC:
        tmp.append(encode(p))
    print('ZOC', tmp)
   
 
    # check if depots in/out of ZOC
    tmp = []
    for depot in depots:
        row, col = decode_coord(depot)
        if (row, col) not in ZOC:
            tmp.append((row, col))
            tmp_map[row][col] = 'D'
    depots = tmp[:]
    if not depots:
        return None
    # just to see
    tmp = []
    for p in depots:
        tmp.append(encode(p))
    #print('depots', tmp)

    # find number of steps from start for every cell in map
    
    result = []
    for depot in depots:
        if depot in ZOC:
            continue
        
        
        row, col = decode_coord(you)
        start = (row, col)
        visited = [start]               
        count = 0                       #number of steps from map
        tmp_map[row][col] = count
        ok = False                      # flag point = depot
        while True:
            change = False
            for i, r in enumerate(tmp_map):
                for j, c in enumerate(r):
                    
                    if c == count:
                        if j % 2 == 0:
                            checks = checks_even
                        else:
                            checks = checks_odd
                        for check in checks:
                            x = i + check[0]
                            y = j + check[1]
                            if 0 <= x <= 8 and 0 <= y <= 11:
                                point = (x, y)
                                if point == depot:
                                    visited.append(point)
                                    #tmp_map[x][y] = count  + 1
                                    result.append(count + 1)
                                    ok = True
                                    break
                                if point not in visited and point not in ZOC:
                                    tmp_map[x][y] = count  + 1
                                    visited.append(point)
                                    change = True
                
            if not change:
                if not result:
                    return None     # depots can't be reached
                else:
                    break           # nothing during cycle
            if not ok:
                count += 1
                '''
                for i in tmp_map:       # print our map step by step
                    print(i)
                print()'''
            else:
                break
        
        for i in tmp_map:       # print our map
            print(i)
        print()
        
    print(result)
    return min(result)

print(supply_line("B7",["C2"],["E3","E4","L1","H2","C3","E8"]))
'''
if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("A3", {"A9", "F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')
'''
