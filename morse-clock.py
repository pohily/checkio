def checkio(time_string: str) -> str:
    result = [[],[],[], [],[],[], [],[]]
    pattern = [2, 4, 0, 3, 4, 0, 3, 4]
    count = 0
    output = ''
    correct = time_string.split(':')
    for i, v in enumerate(correct):
        if len(v) == 1:
            correct[i] = '0' + v
    time_string = ':'.join(correct)
    print(time_string)
    for num in time_string:
        if result[count] == ' : ':
            count += 1
        if num != ':':
            x = bin(int(num))[2:]
            for i in x:
                if i == '1':
                    result[count].append('-')
                else:
                    result[count].append('.')
        count += 1
    print(result)
    for index, elem in enumerate(result):
        if pattern[index] == 0:
            output += ' : '
        else:
            zeros = pattern[index] - len(elem)
            if zeros:
                k = ''.join(elem)
                output += '.'*zeros + k
            else:
                k = ''.join(elem)
                output += k
            if 0< pattern[index]<4:
                output += ' '
    return output

print(checkio("00:1:02"))    


"""

    """


