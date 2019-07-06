def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    
    data_set = set(data)
    m = 0
    l = None
    for elem in data_set:
        if data.count(elem) > m:
            m = data.count(elem)
            l = elem
    return l

print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))

