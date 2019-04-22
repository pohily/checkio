def nearest_square(number):
    from math import sqrt, ceil, floor
    up = ceil(sqrt(number))
    down = floor(sqrt(number))
    return up**2 if abs(up**2 - number) < abs(down**2 - number) else down**2


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")