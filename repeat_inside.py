def repeat_inside(line):
    repeat = ''
    for l in range(1, len(line)//2+1):
        for p in range(len(line) - l):
            count = 2
            check = line[p:p+l]
            if check * count in line:
                while check * count in line:
                    count += 1
                if len(check * (count-1)) > len(repeat):
                    repeat = check * (count-1)
    return repeat
print(repeat_inside('abc'))
