def flip(arr, i, j):
    # flip a panel
    if i < 0 or j < 0:
        return 0
    try:
        if arr[i][j] == '1':
            arr[i][j] = '0'
        else:
            arr[i][j] = '1'
    except IndexError:
        pass
    return arr

def push(a, b, c):
    # make a push on panel: flip the panel and its neighbors
    flip(a, b-1,c)
    flip(a, b, c)
    flip(a, b, c-1)
    flip(a, b, c+1)
    flip(a, b+1, c)
    return a

def chase(on_pan):
    # chase the lighted panels starting from up to bottom row
    result = []
    for row in range(4):
        for col in range(5):
            if on_pan[row][col] == '1':
                push(on_pan, row+1, col)
                result.append(row*5 + col+1+5)
            # just print to see
            print('r', row+1, 'c', col+1)
            for i in on_pan:
                print(''.join(i))
            print()
    return (result, on_pan)
def wall_keeper(on_panels):
    def remove_doubles(arr):
        '''
        This for removing steps which made even number of times since that's redundant
        '''
        rd = sorted(set(arr))
        r = rd[:]
        for i in r:
            if arr.count(i) % 2 == 0:
                rd.remove(i)
        return rd
        
    from copy import deepcopy
    key = {
            '10001':[1, 2], 
            '01010':[1, 4], 
            '11100':[2],
            '00111':[4],
            '10110':[5],
            '01101':[1],
            '11011':[3]
            }
    # init matrix
    start = [['0','0','0','0','0'], ['0', '0','0','0','0'], ['0', '0','0','0','0'], ['0', '0','0','0','0'], ['0', '0','0','0','0']]
    board = deepcopy(start)
    for i in on_panels:
        board[(i-1)//5][i%5 - 1] = '1'
    for i in board:
        print(''.join(i))
    print()
    
    # 1st run of chase the lights
    print('First_____________________________')
    res, board = chase(board)
    
    # check finish on first attempt
    if board == start:
        print('Done')
        return remove_doubles(res)
    
    # check last row
    tmp = ''.join(board[-1])
    if tmp in key:
        res += key[tmp]
        for i in key[tmp]:
            push(board, 0, i-1)
    else:
        return []

    # 2nd run of chase the lights
    print('Second_____________________________')
    res1, board = chase(board)
    
    # check finish on second attempt
    if board == start:
        print('Done')
        return remove_doubles(res + res1)
    return [] 
print(wall_keeper([5, 7, 13, 14, 18]))
