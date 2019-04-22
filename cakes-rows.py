def checkio(cakes):
    from itertools import combinations
    # make a tuple for every cake
    cakes = [tuple(cake) for cake in cakes]
    print('c', cakes)
    # find all lines going through any two points
    pairs = combinations(cakes, 2)
    print('p', pairs)
    rows = set()
    for pair in pairs:
        quantity = 2
        tmp = set()
        tmp.add(pair[0])
        tmp.add(pair[1])
        for point in cakes:
            if point != pair[0] and point != pair[1]:
                dx1 = pair[1][0] - pair[0][0]
                dy1 = pair[1][1] - pair[0][1]
                dx = point[0] - pair[0][0]
                dy = point[1] - pair[0][1]
                s = dx1*dy - dx*dy1
                if s == 0:
                    tmp.add(point)
                    quantity += 1
        if quantity > 2:
            tmp = frozenset(tmp)
            rows.add(tmp)
            
    print(rows)
    
    return len(rows)

print(checkio([[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2], [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]))
'''
"""

'''
