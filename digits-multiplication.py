def checkio(number: int) -> int:
    number = str(number)
    result = 1
    for digit in number:
        if digit != '0':
            result *= int(digit)
    return result

print(checkio(123405))

