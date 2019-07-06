def largest_histogram(histogram):
    ### vert
    result = max(histogram)
    ### hor
    if result < len(histogram):
        tmp = 0
        for i in histogram:
            if i > 0:
                tmp += 1
            else:
                break
        if result < tmp:
            result = tmp
    ### rect
    
    for start in range(len(histogram)):
        v = 0
        h = 0
        m = h*v
        for i in histogram[start:]:
            if i > 1:
                if v == 0:
                    v = i
                    h += 1
                    m = v*h
                else:
                    if i < v:
                        v = i
                        h += 1
                        m = v*h
                    else:
                        h += 1
                        m = v*h
            else:
                if result < m:
                    result = m
                    v = 0
                    h = 0
                else:
                    v = 0
                    h = 0
        if result < m:
            result = m
    return result

print(largest_histogram([1, 1, 5, 3]))
"""

    """


