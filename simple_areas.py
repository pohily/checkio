def simple_areas(*args):
    from math import pi, sqrt
    if len(args) == 1:
        return round(pi * (args[0] / 2)**2, 2)
    elif len(args) == 2:
        return round(args[0]*args[1], 2)
    else:
        p = sum(args) / 2
        return round(sqrt(p * (p-args[0]) * (p-args[1]) * (p-args[2])), 2)

print(simple_areas(1.5, 2.5, 2))
