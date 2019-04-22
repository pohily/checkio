def safe_code(equation):
    from operator import sub, add, mul
    do_it = {'-':sub, '+':add, '*':mul}
    copy = equation
    equation = equation[::-1]
    symbol = last = second = first = oper = '' 
    while symbol != '=':
        symbol = equation[0]
        equation = equation[1:]
        last += symbol 
    last = last[:-1]
    last = last[::-1]

    symbol = equation[0]
    while symbol == '#' or symbol.isdigit():
        symbol = equation[0]
        equation = equation[1:]
        second += symbol 
    second = second[:-1]
    second = second[::-1]
    if (symbol == '-' and equation[0] == '-') or (symbol == '-' and equation[0] == '+') or (symbol == '-' and equation[0] == '*'):
        second += '-'
        second = second[::-1]
        oper = equation[0]
        equation = equation[1:]
    else:
        oper = symbol
    first = equation[::-1]
    check = first+second+last
    for i in range(10):
        if str(i) in check:
            print(i, ' is already in the equation')
            continue
        else:
            if i == 0 and first[0] == '#' or i == 0 and second[0] == '#' or i == 0 and last[0] == '#':
                continue
            f = int(first.replace('#', str(i)))
            s = int(second.replace('#', str(i)))
            l = int(last.replace('#', str(i)))
            if do_it[oper](f, s) == l:
                print(copy.replace('#', str(i)))
                return i
    return -1

print(safe_code("24-35=-##"))
