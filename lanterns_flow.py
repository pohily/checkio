def lanterns_flow(river_map, minutes):
    num = river_map[0].count('.')
    river_map = list(river_map)
    river_map[0] = river_map[0].replace('.', 'L')
    if minutes == 0:
        return num * 2
    # draw path for every lantern (P - passed time, L - lantern)

    for lanterns in range(num):
        for time in range(1, minutes+1):
            river_map[time-1] = river_map[time-1].replace('L', 'P', 1) #mark passed
            #### пока без поворотов
            river_map[time] = river_map[time].replace('.', 'L', 1) #new position
    
    # mark lighted (l - lighted, D - counted), then count l and D
    count = 0
    for lantern in range(num):
        for row in range(len(river_map)):
            if 'L' in river_map[row]:
                col = river_map[row].find('L')
                # count
                a = [-1, 0, 1]
                for j in a[:2]:
                    for i in a:
                        if river_map[row+j][col+i] == '.' or river_map[row+j][col+i] == 'P':
                            count += 1
                            river_map[row+j] = river_map[row+j][:col+i] + 'l' + river_map[row+j][col+i+1:]
                        river_map[row] = river_map[row][:col] + 'D' + river_map[row][col+1:]
                if row+1 < len(river_map):
                    for i in a:
                        if river_map[row+1][col+i] == '.' or river_map[row+1][col+i] == 'P':
                            count += 1
                            river_map[row+1] = river_map[row+1][:col+i] + 'l' + river_map[row+1][col+i+1:]
                        river_map[row] = river_map[row][:col] + 'D' + river_map[row][col+1:]
                break
            

    print(river_map)
    return count + num
        

print(lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 4))  
"""

"""               



