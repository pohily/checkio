def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    change = True
    while change:
        change = False
        for i in intervals:
            for j in intervals:
                if i != j:
                    if (i[1] + 1 == j[0]) or (i[1] >= j[0] and i[1] <= j[1]) or(i[1] >= j[1] and i[0] <= j[1]) or (i[0] -1 == j[1]):
                        intervals.append((min(i[0], i[1], j[0], j[1]), max(i[0], i[1], j[0], j[1])))
                        change = True
                        intervals.remove(i)
                        intervals.remove(j)
                        break
            break
    return sorted(intervals)

print(merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]))
                    



