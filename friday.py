def friday(day):
    from datetime import datetime
    start = datetime.strptime(day, "%d.%m.%Y")
    finish = 5 - start.isoweekday()
    return finish if finish >=0 else 7 + finish

print(friday('22.03.2019'))
'''
if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
