def convert(numerator, denominator):
    whole = str(numerator // denominator)
    fraction, num = '', []
    if numerator % denominator != 0:
        numerator %= denominator
        while True:
            numerator *=10
            if numerator % denominator != 0:
                fraction += str(numerator // denominator)
                num.append(numerator)
                numerator %= denominator

                # check for cycle
                if len(fraction) > 1:
                    for i in range(len(fraction)//2):
                        if fraction[len(fraction)-(i+1):]*2 == fraction[len(fraction)-(i+1)*2:] and num[-(i+1)] == num[-(i+1)*2]:
                            cycle = fraction[len(fraction)-(i+1):]
                            precycle = fraction[:len(fraction)-(i+1)*2]
                            return whole + '.' + precycle + '(' + cycle +')'
            else:
                fraction += str(numerator // denominator)
                return whole + '.' + fraction
    return whole + '.' + fraction
     
print(convert(0, 117))  
"""
def convert(numerator, denominator):
    q, r = divmod(numerator, denominator)
    result = str(q) + '.'
    remainders = [r]
    while r:
        q, r = divmod(r * 10, denominator)
        result += str(q)
        if r in remainders:
            pos = remainders.index(r) - len(remainders)
            return result[:pos] + '(' + result[pos:] + ')'
        remainders.append(r)
    return result
"""               



