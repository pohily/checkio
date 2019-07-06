def checkio(data):
    data = str(data)
    rank = len(data)
    result = ''
    roman = [[], ['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']]
    for r in data:
        if int(r) < 4:
            result += int(r) * roman[rank][0]
        elif int(r) == 4:
            result += roman[rank][0] + roman[rank][1]
        elif 4 < int(r) < 9:
            result += roman[rank][1] + (roman[rank][0] * (int(r) - 5))
        elif int(r) == 9:
            result += roman[rank][0] + roman[rank+1][0]
        rank -= 1
    return result


print(checkio("571"))
"""

    """


