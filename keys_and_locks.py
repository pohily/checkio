def cut(arr):
    #cut excess material from up and left
    u = l = 0
    for index, row in enumerate(arr):
        if '#' in row:
            u = index 
            l = row.index('#')
            break
    for row in arr:
        if '#' in row:
            if row.index('#') < l:
                l = row.index('#')
    # cut up
    if u > 0:
        for i in range(u):
            del arr[0]
    # cut left
    if l > 0:
        new_arr = []
        for row in arr:
            tmp = []
            for i in range(l, len(row)):
                tmp.append(row[i])
            new_arr.append(tmp)
        return new_arr  
    return arr


def turn(smth):
    # turn matrix on 90
    smth = list(zip(*smth))
    for i, v in enumerate(smth):
        smth[i] = list(v)
    return smth[::-1]


def keys_and_locks(lock, some_key):
    # init key and lock
    lock = lock.split()
    some_key = some_key.split()
    for i, v in enumerate(lock):
        lock[i] = list(v)
    for i, v in enumerate(some_key):
        some_key[i] = list(v)
    
    # cut excess from key and lock    
    lock = cut(lock)
    some_key = cut(some_key)
    
    # turn them upside down
    lock = turn(lock)
    lock = turn(lock)
    some_key = turn(some_key)
    some_key = turn(some_key)
    
    # and cut again from other side
    lock = cut(lock)
    some_key = cut(some_key)
    
    # make copies of key turned to 90, 180, 270
    keys = [some_key]
    key90 = turn(some_key)
    key180 = turn(key90)
    key270 = turn(key180)
    keys += [key90]+[key180]+[key270]
    
    # compare lock and all the copies of the key
    for key in keys:
        if lock == key:
            return True
    return False
print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))
