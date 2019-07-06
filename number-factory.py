def check(num):
    for i in reversed(range(2, 10)):
        if num % i == 0:
            return num // i
    return -1

def checkio(number):
    result = []
    et = number
    ost = check(number)
    while ost > 0:
        result.append(str(number // ost))
        number = ost
        ost = check(number)
    if result:
        tmp = 1
        for i in result:
            tmp *= int(i)
        if tmp != et:
            return 0
        else:
            result = ''.join(sorted(result))
                
                
    else:
        return 0
    return int(result)


print(checkio(40))
"""

    """


