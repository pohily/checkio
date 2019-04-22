def greatest_common_divisor(*args):
    """
        Find the greatest common divisor with Euclidean algorithm
    """
    args = list(args)
    while len(args) > 1:
        m = min(args)
        args = [x % m for x in args if x % m > 0] + [m]
    return args[0] if args else m

print(greatest_common_divisor(3, 9, 3, 9))
