def checkio(numbers_array: tuple) -> list:
    tmp = sorted([(abs(x), x) for x in numbers_array])

    return [x for (y, x) in tmp]

print(checkio((-20, -5, 10, 15)))

