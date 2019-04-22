def checkio(year):
    from datetime import date
    result = 0
    for month in range(1, 13):
        day = date(year, month, 13)
        if day.isoweekday() == 5:
            result += 1
    return result
    
print(checkio(2019))


"""
def checkio(year):
    """
    calendar.weekday(year, month, day)
        Returns the day of the week
    """
    c = 0
    for i in range(1, 13):
        if calendar.weekday(year, i, 13) == calendar.FRIDAY:
            c += 1
    return c
"""               



