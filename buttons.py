def buttons(ceiling):
    def check(point):
        # check point and its 4 neighbours, add non-zero neighbours to cont - for next check and return value of current point
        try:
            if (point[0]+1, point[1]) in coords:
                coords.remove((point[0]+1, point[1]))
                if  ceiling[point[0]+1][point[1]] != '0':
                    cont.append((point[0]+1, point[1]))
        except IndexError:
            pass
        try:
            if (point[0], point[1]+1) in coords:
                coords.remove((point[0], point[1]+1))
                if  ceiling[point[0]][point[1]+1] != '0':
                    cont.append((point[0], point[1]+1))
        except IndexError:
            pass
        try:
            if (point[0]-1, point[1]) in coords:
                coords.remove((point[0]-1, point[1]))
                if  ceiling[point[0]-1][point[1]] != '0':
                    cont.append((point[0]-1, point[1]))
        except IndexError:
            pass
        try:
            if (point[0], point[1]-1) in coords:
                coords.remove((point[0], point[1]-1))
                if  ceiling[point[0]][point[1]-1] != '0':
                    cont.append((point[0], point[1]-1))
        except IndexError:
            pass
        return int(ceiling[point[0]][point[1]])

    cont, values = [], []
    # init list of ceiling coordinates
    ceiling = ceiling.split()
    coords = [(i, j) for i in range(len(ceiling)) for j in range(len(ceiling[0]))]
    
    # check all the coords of ceiling
    while coords:
        cur = coords[0]
        coords = coords[1:]
        if ceiling[cur[0]][cur[1]] == '0':
            continue
        else:
            # count value for the point of the button
            values.append(0) # new button
            values[-1] += check(cur)
            # count value for neighbour points of the button
            while cont:
                cur_v = cont[0]
                cont = cont[1:]
                values[-1] += check(cur_v)
        print('values', values)
    return sorted(values, reverse=True)


print(buttons('''
001203
023001
100220'''))
"""

"""
