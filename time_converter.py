def time_converter(time):
    x = time.index(':')
    h = int(time[:x])
    half = time[-4]
    result = ''
    if h == 12:
        h = 0
    if 0 <= h <= 9 and half == "a":
        result += '0'
    if half == "p":
        h += 12
    return result + str(h) + time[x:x+3]

print(time_converter('6:50 p.m.'))
"""

    """


