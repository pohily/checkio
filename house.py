def house(plan):
    plan = plan.split()
    u = 0
    d = 0
    l = 0
    r = 0
    for index, row in enumerate(plan):
        if '#' in row:
            u = index 
            l = row.index('#')
            break
    for row in plan:
        if '#' in row:
            if row.index('#') < l:
                l = row.index('#')
    
    plan = plan[::-1]
    for index, row in enumerate(plan):
        if '#' in row:
            tmp = row[::-1]
            d = len(plan) - index - 1 
            r = len(row) - tmp.index('#') - 1
            break
    for row in plan:
        if '#' in row:
            tmp = row[::-1]
            if len(row) - tmp.index('#') - 1 > r:
                r = len(row) - tmp.index('#') - 1
                
    print("u", u, "l", l, "d", d, "r", r)
    if u == 0 and d == 0 and l == 0 and r == 0: return 0
    return (d - u + 1) * (r - l + 1)

print(house('''0000
0000
#000
'''))


