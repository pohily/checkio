def checkio(number):
    start = 1
    end = 1
    result = []
    sum_result = 0
    while True:
        while sum_result < number:
            t_r = end * (end + 1) // 2
            if t_r > number:
                return []
            result.append(t_r)
            sum_result += t_r
            end += 1
        if sum_result == number:
            return result
        while sum_result > number:
            t_l = start * (start + 1) // 2
            if t_l > number:
                return []
            result.remove(t_l)
            sum_result -= t_l
            start += 1
        if sum_result == number:
            return result
        
            

print(checkio(882))
                    



