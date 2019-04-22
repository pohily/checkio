def divide_pie(groups):
    from math import gcd
    quantity = sum([abs(x) for x in groups])
    reminder = (1, 1)
    for group in groups:
        if group > 0:
            reminder = (reminder[0] * quantity - group * reminder[1], reminder[1] * quantity)
        else:  
            reminder = (reminder[0] * (quantity + group), reminder[1] * quantity)
        reminder = int(reminder[0]), int(reminder[1])
        reminder = reminder[0]/gcd(reminder[0], reminder[1]), reminder[1]/gcd(reminder[0], reminder[1])
    return reminder

print(divide_pie((1, -2, 3)))
"""
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
"""
