def time_converter(time):
    hour = int(time[:2])
    if hour == 0:
        hour = 12
        suffix = ' a.m.'
    elif 1 <= hour <= 11:
        suffix = ' a.m.'
    elif hour == 12:
        suffix = ' p.m.'
    elif hour > 12:
        suffix = ' p.m.'
        hour -= 12
    return str(hour) + time[2:] + suffix


print(time_converter('09:30'))
"""

"""               



