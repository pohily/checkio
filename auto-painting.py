def checkio(capacity, number):
    from math import ceil
    items = ''.join([str(i) for i in range(number)])
    result = []
    if number <= capacity:
            result.append(items)
            result.append(items)
    
    elif number % capacity == 0:
        for i in range(ceil(number / capacity)):
                x = items[0+i*capacity:1*capacity + i*capacity]
                result.append(x)
                result.append(x)
    else:
        while number / capacity > 1.5:
            number -= capacity
            result.append(items[:capacity])
            result.append(items[:capacity])
            items = items[capacity:]
        
        result.append(items[:capacity])
        result.append(items[:number-capacity]+items[capacity:])
        result.append(items[number-capacity:capacity]+items[capacity:])
        
    return ','.join(result)

print(checkio(3, 6))

'''
def checkio(capacity, number):
    ret = [str(x) for x in list(range(number))*2]
    ret = __import__('textwrap').wrap(''.join(ret), min(capacity, number))
    return ','.join(sorted(ret))

'''