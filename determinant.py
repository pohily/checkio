def checkio(data):
    sign = 1
    # for each row from last to second: rows 2, 1 but not 0
    for i in range(len(data)-1, 0, -1):
        # make triangle matrix
        for j in range(i):
            # check if 0 on diag - then swap rows and sign
            if data[len(data) - i - 1][len(data) - i - 1] == 0:
                for count in range(len(data) - i, len(data)):
                    if data[count][len(data) - i - 1] != 0:
                        data[count], data[len(data) - i - 1] = data[len(data) - i - 1], data[count]
                        sign *= -1
                        break
                        
            # k - difference 1)... 3-0, 2-0, 1-0 and 0-0; 2)... 3-1, 2-1 and 1-1; 3) ... 3-2 and 2-2    
            k = data[len(data) - j - 1][len(data) - i - 1] / data[len(data) - i - 1][len(data) - i - 1]
            tmp = []
            for index, elem in enumerate(data[len(data) - j - 1]):
                tmp.append(elem - data[len(data) - i - 1][index] * k)
            data[len(data) - j - 1] = tmp[:]
    # count determinant
    result = 1
    for i in range(len(data)):
        result *= data[i][i]
    return round(result * sign)

print(checkio([
    [0,4,2],
    [9,3,2],
    [3,9,5]]))

'''
#from numpy.linalg import det as checkio

def checkio(data):
    if len(data) == 1:
        return data[0][0]
    result = 0
    for i, row in enumerate(data):
        result += (-1) ** i * row[0] * checkio([r[1:] for j, r in enumerate(data) if i != j])
    return result

'''
