def checkio(first, second):
    first = bin(first)[2:]
    second = bin(second)[2:]
    a, o, x = 0, 0, 0
    #and
    for i in first:
        tmp = ''
        for j in second:
            tmp += str(int(i) & int(j))
            print(int(i) & int(j))
        print('a', a)
        a += int(tmp, 2)
    #or
    for i in first:
        tmp = ''
        for j in second:
            tmp += str(int(i) | int(j))
            print(int(i) & int(j))
        print('o', o)
        o += int(tmp, 2)
    #xor
    for i in first:
        tmp = ''
        for j in second:
            tmp += str(int(i) ^ int(j))
            print(int(i) & int(j))
        print('x', x)
        x += int(tmp, 2)
    return a + o + x
print(checkio(4, 6))

"""
def checkio(first, second):
    
    AND=lambda x, y: x and y 
    OR=lambda x, y: x or y 
    XOR=lambda x, y: (not x and y) or (x and not y)
    
    def logical_op(x, y, op):
        return sum(int(''.join('1' if op(int(i), int(j)) else '0' for j in y), 2) for i in x)
        
    first=bin(first)[2:]
    second=bin(second)[2:]
    operators=[AND, OR, XOR]
        
    return sum(logical_op(first, second, op) for op in operators)
"""
                    



