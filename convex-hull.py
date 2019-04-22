def checkio(data):
    '''Graham scan'''
    from math import sqrt

    # find bottom leftmost point p0
    x, y = data[0]
    for p in data[1:]:
        i, j = p
        if j < y:
            x, y = p
        elif j == y and i < x:
            x, y = p
    p0 = [x, y]

    # make a stack of points sorted by polar angle btw p0-pi and x-axis
    stack = [p0] 
    angles = {}     # cosin = point
    rest_of_data = [i for i in data if i != p0] #without p0
    for point in rest_of_data:
        i, j = point
        #cosin = (x * i + y * j) / (sqrt(x**2 + y**2) * sqrt(i**2 + j**2))
        cosin = abs((i-x) / (sqrt((i-x)**2 + (j-y)**2)))
        angles[cosin] = point
    print(angles)
    for elem in sorted(angles.keys()):
        stack.append(angles[elem])
    print(stack)
    
    # look if turn p0 - p1 - p2 is left or right: if left pop the turn point
    remove = False
    while True:
        l = len(stack)
        for i in range(l):
            x1, y1 = stack[i]
            x2, y2 = stack[(i + 1) % l]
            x3, y3 = stack[(i + 2) % l]
            turn = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if turn < 0:
                stack.remove([x2, y2]) #second point must be removed
                remove = True
                break
        if remove:
            remove = False
            continue
        else:
            result = [data.index(i) for i in stack]
            result = [result[0]] + result[1:][::-1]
            return result




print(checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
'''
