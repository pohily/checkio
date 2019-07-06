def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    from math import floor, ceil
    number = float(number)
    power, trail = 0, ''
    while abs(number) >= base and power < len(powers)-1:
        number = number / base
        power += 1
    if decimals:
        number = round(number, decimals)
    else:
        if number >= 0:
            number = floor(number)
        else:
            number = ceil(number)
    number = str(number)
    try:
        x = len(number[number.index('.')+1:])
        if x < decimals:
            trail = '0'*(decimals - x)
    except ValueError:
        if decimals == 0:
            trail = ''
        else:
            trail = '.' + '0' * decimals

    return str(number) + trail + powers[power] + suffix

print(friendly_number(10**32))    


"""

    """


