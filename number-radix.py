def checkio(str_number: str, radix: int) -> int:
    str_number = str_number[::-1]
    result = 0
    power = 0
    for digit in str_number:
        ### check
        if digit.isalpha():
            if (ord(digit) - 55) >= radix:
                return -1
        else:
            if int(digit) >= radix:
                return -1

        ### count
        if digit.isalpha():
            result += pow(radix, power) * (ord(digit) - 55)
        else:
            result += pow(radix, power) * int(digit)
        power += 1
    return result

print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("101", 5))
print(checkio("Z", 36))
print(checkio("AB", 10))

