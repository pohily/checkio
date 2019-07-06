def checkio(number):
    s, count = 0, 0
    while s <= number:
        count += 1
        s += count*(1+count)//2
    if s > number:
        if s - number > count:
            return count*(count-1)//2
        else:
            return count*(1+count)//2 - (s - number)
    else:
        return count*(1+count)//2
print(checkio(10))    


"""


    """


