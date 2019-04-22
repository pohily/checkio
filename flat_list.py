def flat_list(array):
    result = []
    unpacked = True
    while unpacked:
        unpacked = False
        if result:
            array = result[:]
        result = []
        while array:
            if isinstance(array[0], list):
                result.extend(array.pop(0))
                unpacked = True
            else:
                result.append(array.pop(0))
    return result




print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
"""
def flat_list(array):
    if not isinstance(array, list):
        return [array]
    res = []
    for v in array:
        res += flat_list(v)
    return res



#marta vohnoutova
def flat_list(l_in):
   import re
   l=re.split('\[|\]|\,',str(l_in))
   return [int(i) for i in l if i not in ('',' ')] 



def flat_list(array):
    collected = []
    for item in array:
        if isinstance(item, list):
            collected.extend(flat_list(item))
        else:
            collected.append(item)
    return collected
"""               



