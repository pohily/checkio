def tower(cubes):
    
    # right roll - main. make 4 times and return 4 states
    def rr(k):
        f, r, l, b, t, d = k
        res = []
        for i in range(4):
            f, r, b, l = r, b, l, f #turn the cube
            res.append(''.join([f, r, l, b]))
        return sorted(res)
        
    # back flip make 4 times, after each time make right roll
    def bf(k):
        f, r, l, b, t, d = k
        t, b, d, f = b, d, f, t
        k = ''.join([f, r, l, b, t, d])
        return k
    
    # right flip make 1 time and then right roll
    def rf(k):
        f, r, l, b, t, d = k
        t, l, d, r = r, t, l, d
        k = ''.join([f, r, l, b, t, d])
        return k
    
    # swap make 1 time and then right roll
    def swap(k):
        f, r, l, b, t, d = k
        f, b, t, d = b, f, d, t
        k = ''.join([f, r, l, b, t, d])
        return k

    # make 24 states for each cube
    states = [] 
    for cube in cubes:
        tmp = []
        for i in range(4):
            tmp.append(rr(cube))
            cube = bf(cube)
        cube = rf(cube)
        tmp.append(rr(cube))
        cube = swap(cube)
        tmp.append(rr(cube))
        states.append(tmp)
    
    # find max intersection of states
    print(states)
    max_intersect = 0
    for state in states:
        for s in state:
            tmp = 0
            for check in states:
                if s in check:
                    tmp += 1 
            if tmp > max_intersect:
                max_intersect = tmp
                most_comm = s 
    print('most_comm', most_comm)    
    return max_intersect


print(tower(["GYCABW","ARCGYW","RGBCAW","RGBCAY","OCYWBA","WCAVBR","ACYVWR","OCYWBA","WCAVBR","ACYVWR"]))


'''
import collections

def tower(cubes):
    twr, sdx = [], ['0132', '1320', '3201', '2013',
                    '0231', '2310', '3102', '1023',
                    '0435', '4350', '3504', '5043',
                    '1524', '5241', '2415', '4152',
                    '0534', '5340', '3405', '4053',
                    '1425', '4251', '2514', '5142']
    for cube in cubes:
        for i in sdx:
            t = ''
            for j in i:
                t += cube[int(j)]
            twr += [t]           
    return max(collections.Counter(twr).values())




from itertools import chain
def tower(cubes):
    
    for i, cube in enumerate(cubes):
        # Getting all of the axes of the cube.
        cubes[i] = [cube[:2] + cube[3] + cube[2],
                    cube[0] + cube[5] + cube[3] + cube[4],
                    cube[1] + cube[4] + cube[2] + cube[5]]
        # Standartising axes.
        for s, axis in enumerate(cubes[i]):
            cubes[i][s] = (axis[axis.index(max(axis)):] +
                           axis[:axis.index(max(axis))])
            if cubes[i][s][1] > cubes[i][s][-1]:
                cubes[i][s] = cubes[i][s][0] + cubes[i][s][:0:-1]
    all_axes = tuple(chain(*cubes))
    return max(all_axes.count(axis) for axis in set(all_axes))
'''
    
    
    

