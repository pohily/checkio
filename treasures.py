def treasures(info, limit):
    limit *= 1000
    take = []
    # find most valuable item
    value = []
    for item in info:
        value.append((info[item]['price'] / info[item]['weight'], item))
    for item in sorted(value, reverse=True):
        take.append(item[1])
    
    # find what we take
    for item in take:
        info[item]['take'] = 0
        while info[item]['amount'] and info[item]['weight'] <= limit:
            info[item]['take'] += 1
            limit -= info[item]['weight']
            info[item]['amount'] -= 1
    
    # result output
    take = ['golden coin', 'silver coin', 'ruby']         
    result = []
    for item in take:
        if info[item]['take']:
            tmp = info[item]['take']
            result += [item + f": {tmp}"]
        
    print(limit)
    return result

print(treasures({
    "silver coin":{"price":10,"amount":100,"weight":10},
    "ruby":{"price":1000,"amount":5,"weight":200},
    "golden coin":{"price":100,"amount":100,"weight":10}},1.8))

"""

"""
