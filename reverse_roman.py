def reverse_roman(roman_string):
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    result = 0
    ex = ['IV', 'IX', 'XC', 'CD', 'CM']
    for x in ex:
        if x in roman_string:
            start = roman_string.index(x)
            roman_string = roman_string[:start]+roman_string[start+2:]
            result += (roman[x[1]] - roman[x[0]])
    if roman_string:
        for letter in roman_string:
            result += roman[letter]
    return result
    

print(reverse_roman('LXXVI'))
"""

    """


