def pr_on(lighted):
    for i in range(5):
        tmp = ''
        for j in range(1, 6):
            if i*5+j in lighted:
                tmp += '1'
            else:
                tmp += '0'
        print(tmp)
    print()


def chase(on_pan):
    result = []
    pr_on(on_pan)
    for row in range(1, 5):
        for panel in range((row-1)*5 + 1, row * 5 + 1):
            if panel in on_pan:
                on_pan.remove(panel)
                result.append(panel+5)
                # if lights are off, switch it on
                for a in range(4, 7):
                    if panel+a not in on_pan:
                        on_pan.append(panel+a)
                    else:
                        on_pan.remove(panel+a)
                #check down
                if row < 4:
                    if panel+10 not in on_pan:
                        on_pan.append(panel+10)
                    else:
                        on_pan.remove(panel+10)
                # switch off lights that were on, but they are on wrong row
                #check left
                if panel == (row-1)*5 + 1:
                    on_pan.remove(panel+4)
                #check right
                if panel == row * 5:
                    on_pan.remove(panel+6)
            print('r', row, 'p', panel)
            pr_on(on_pan)
    return (result, on_pan)


def wall_keeper(on_panels):
    key = {
            '10001':([1, 2], [1, 2, 3, 6, 7]), 
            '01010':([1, 4], [1, 2, 3, 4, 5, 6, 9]), 
            '11100':([2], [1, 2, 3, 7]),
            '00111':([4], [3, 4, 5, 9]),
            '10110':([5], [4, 5, 10]),
            '01101':([1], [1, 2, 6]),
            '11011':([3], [2, 3, 4, 8]),
            }
    # 1st run of chase the lights
    print('First_____________________________')
    res, on_panels = chase(on_panels)
    
    # check last row
    tmp = ''
    for j in range(1, 6):
        if 20+j in on_panels:
            tmp += '1'
        else:
            tmp += '0'
    if tmp in key:
        res += key[tmp][0]
        on_panels += key[tmp][1]
    else:
        return []

    # 2nd run of chase the lights
    print('Second_____________________________')
    res1, on_panels = chase(on_panels)
    return res + res1
print(wall_keeper([5, 7, 13, 14, 18]))


"""

"""               



