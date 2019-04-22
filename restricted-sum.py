def checkio(data):
    x = data[0]
    data = data[1:]
    if data:
        data[0] += x
    
    return x if not data else checkio(data)



print(checkio([1, 2, 3, 4]))
