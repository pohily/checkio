def date_time(time: str) -> str:
    calendar = {'01':' January ', '02':' February ', '03':' March ', '04':' April ', '05':' May ', '06':' June ', '07':' July ', '08':' August ', '09':' September ', '10':' October ', '11':' November ', '12':' December '}
    result = str(int(time[:2])) + calendar[time[3:5]] + time[6:11] + 'year '
    h = int(time[11:13])
    m = int(time[14:])
    if h == 1:
        result += str(h) + ' hour '
    else:
        result += str(h) + ' hours '
    if m == 1:
        result += str(m) + ' minute'
    else:
        result += str(m) + ' minutes'
    return result

print(date_time('20.11.1990 03:55'))
"""

    """


