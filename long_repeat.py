def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    char = line[0]
    result = 1
    max_result = 1
    for letter in line[1:]:
        if letter == char:
            result +=1
        else:
            if max_result < result:
                max_result = result
            result = 1
            char = letter
    if max_result < result:
                max_result = result
    return max_result
    
print(long_repeat('ddvvrwwwrggg'))

"""
import re
def long_repeat(line):
    count = 0
    for i in set(line):
        max_line = re.findall('['+str(i)+']+',line)
        for j in max_line:
            if len(j) > count:
                count = len(j)
    return count
print(long_repeat('abababaab'))
   
    

def long_repeat(line):
    longest = 0
    while line:
        stripped = line.lstrip(line[0])
        longest = max(longest, len(line) - len(stripped))
        line = stripped
    return longest
    """


