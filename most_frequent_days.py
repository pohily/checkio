import calendar
def most_frequent_days(year):
    from datetime import date
    week = list(calendar.day_name)
    result = [0]*8
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                d = date(year, month, day)
                result[d.isoweekday()] += 1
            except ValueError:
                continue
    m = max(result)
    res = []
    for i, v in enumerate(result):
        if v == m:
            res.append(week[i-1])
    return res
    
print(most_frequent_days(1152))


"""

"""               



