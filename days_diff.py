def days_diff(date1, date2):
    from datetime import date
    
    d1 = date(*date1)
    d2 = date(*date2)
    
    return abs((d2 - d1).days)
    
print(days_diff((1978, 1, 4), (2019, 2, 25)))


"""

"""               



