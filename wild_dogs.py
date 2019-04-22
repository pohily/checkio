def wild_dogs(coords):
    from itertools import combinations
    from math import sqrt
    def distance(line):
        # find distance from (0, 0) to line        
        a = line[0][1] - line[1][1]
        b = line[1][0] - line[0][0]
        c = line[0][0]*line[1][1] - line[1][0]*line[0][1]
        distance = c / sqrt(a**2 + b**2)
        return abs(round(distance, 2))
    # find all lines going through any two points
    pairs = list(combinations(coords, 2))

    # find longest line
    longest = 2
    for pair in pairs:
        quantity = 2
        for point in coords:
            if point != pair[0] and point != pair[1]:
                dx1 = pair[1][0] - pair[0][0]
                dy1 = pair[1][1] - pair[0][1]
                dx = point[0] - pair[0][0]
                dy = point[1] - pair[0][1]
                s = dx1*dy - dx*dy1
                if s == 0:
                    quantity += 1
                    if quantity > longest:
                        longest = quantity
                        longest_line = pair

    # if every line goes through only two points
    if longest == 2:
        d = distance(pairs[0])
        for pair in pairs[1:]:
            cur = distance(pair) 
            if cur < d:
                d = cur
        return d 
    else:
        # find distance to longest line
        return distance(longest_line)
    
print(wild_dogs([(6, -0.5), (3, -5), (1, -20)]))

