def group_equal(els):
    check, result = [], []
    for value in els:
        if value != check:
            check = value
            result.append([value])
        else: 
            result[-1] += [value]
    return result


print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))

"""

""" 
