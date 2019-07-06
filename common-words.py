def checkio(first, second):
    return ','.join(sorted(list(set(first.split(',')) & set(second.split(',')))))


print(checkio("one,two,three", "four,five,one,two,six,three"))
"""

    """


