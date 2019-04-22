from datetime import date, timedelta
def checkio(from_date, to_date):
    result = 0
    for i in range((to_date - from_date).days + 1):
        d = from_date + timedelta(days=i)
        if d.isoweekday() == 6 or d.isoweekday() == 7:
            result += 1
    return result
print(checkio(date(2013, 1, 1), date(2013, 2, 1)))


"""

"""               



