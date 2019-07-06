
def is_prime(num):
    from math import sqrt
    if num % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True
def backwardsPrime(start, stop):
    result = []
    for i in range(start, stop+1):
        j = int(str(i)[::-1])
        if i != j and is_prime(i) and is_prime(j):
            result.append(i)
    return result
print(backwardsPrime(361, 362))

