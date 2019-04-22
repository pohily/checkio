def count_consecutive_summers(num):
    count, low, summ = 0, 1, 0
    for i in range(1, num+1):
        summ += i
        if summ < num:
            print('s', summ, 'l', low, 'i', i)
            continue
        elif summ == num:
            count += 1
            summ -= low
            print('s', summ, 'l', low, 'i', i)
            low += 1
        else:
            while summ >= num:
                summ -= low
                print('s', summ, 'l', low, 'i', i)
                low += 1
                if summ == num:
                    count += 1
                    break
    return count
    
print(count_consecutive_summers(99))

"""

""" 
