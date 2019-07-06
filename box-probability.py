def checkio(marbles: str, step: int) -> float:
    result = [[(marbles, 1)]]
    count = 0
    while step - count-1:
        if len(result) < count + 2:
            result.append([])
        for i in result[count]:
            if 'w' in i[0]:
                tmp = i[0].replace('w', 'b', 1)
                result[count+1].append((tmp, i[1] * i[0].count('w')/len(marbles)))
            if 'b' in i[0]:
                tmp = i[0].replace('b', 'w', 1)
                result[count+1].append((tmp, i[1] * i[0].count('b')/len(marbles)))
        count += 1
    print(result)
    return round(sum([i[1] * i[0].count('w')/len(marbles) for i in result[-1]]), 2)
        
print(checkio('www', 3))
"""

"""               



