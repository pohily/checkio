def checkio(data: list) -> list:
    data_set = set(data)
    for item in data_set:
        if data.count(item) == 1:
            data.remove(item)
    return data
    
print(checkio([1, 2, 3, 1, 3]))

"""
def checkio(d: list) -> list:
    return [x for x in d if d.count(x) != 1]
    """


