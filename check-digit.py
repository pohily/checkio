def checkio(data):
    def reduced(num):
        d = num * 2
        if d <= 9:
            return d
        else:
            return sum([int(x) for x in str(d)])
    # discard all format chars
    total, sanitize = 0, []
    for elem in data:
        if elem.isdigit() or elem.isalpha():
            sanitize.append(elem)
    data = ''.join(sanitize)

    # find total sum
    for index, value in enumerate(data[::-1]):
        if index % 2 == 1:
            if value.isdigit():
                total += int(value)
            else:
                total += ord(value) - 48
        else:
            if value.isdigit():
                total += reduced(int(value))
            if value.isalpha():
                total += reduced(ord(value) - 48)
    if total % 10 == 0:
        result = 0
    else:
        result = 10 - total % 10
    return [str(result), total]


    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("123"))
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")

