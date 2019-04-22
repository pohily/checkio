FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    str_number, result = str(number), ''
    r = len(str_number)
    while r:
        if r == 3:
            result += FIRST_TEN[int(str_number[0]) - 1] + ' ' + HUNDRED
            if str_number[1:] == '00':
                break
            else:
                result += ' '
                r -= 1
                str_number = str_number[1:]
                continue
        if r == 2:
            if str_number[0] == '0':
                str_number = str_number[1:]
                r -= 1
                continue
            if str_number[0] == '1':
                str_number = str_number[1:]
                result += SECOND_TEN[int(str_number[0])]
                break
            else:
                result += OTHER_TENS[int(str_number[0]) - 2]
                if str_number[1] == '0':
                    break
                else:
                    result += ' '
                    str_number = str_number[1:]
                    r -= 1
                    continue
        if r == 1:
            result += FIRST_TEN[int(str_number[0]) - 1]
            break
    return result

print(checkio(270))

"""

""" 
