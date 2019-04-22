def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        if key:
            result = [key(x) for x in args[0]]
            return args[0][result.index(sorted(result)[0])]
        else:
            return sorted(args[0])[0]
    else:
        if key:
            result = [key(x) for x in args]
            return args[result.index(sorted(result)[0])]
        else:
            return sorted(args)[0]
    


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        if key:
            result = [key(x) for x in args[0]]
            return args[0][result.index(sorted(result)[-1])]
        else:
            return sorted(args[0])[-1]
    else:
        if key:
            result = [key(x) for x in args]
            return args[result.index(sorted(result)[-1])]
        else:
            return sorted(args)[-1]


#print(max(2.2, 5.6, 5.9, key=int))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1: args = args[0]
    res = sorted(args, key = key)
    return res[0]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1: args = args[0]
    res = sorted(args, key = key, reverse = True)
    return res[0]

'''



