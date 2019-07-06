def stone_wall(wall):
    wall = wall.split()
    min_width = len(wall)
    result = 0

    for i in range(len(wall[0])):
        width = 0
        for index, row in enumerate(wall):
            if row[i] == '#':
                width += 1
            else:
                ## check for trap
                if index < len(wall) - 1:
                    for y in range(1, len(wall) - index):
                        if wall[index+y][i] == '#':
                            width +=1
                        

                ## check width
                if min_width > width:
                    min_width = width
                    result = i
                    break
    return result
    
    
print(stone_wall('''
##########
00##0##0##
#0######00
'''))


