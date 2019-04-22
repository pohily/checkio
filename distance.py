R = 6371
def distance(first, second):
    from re import findall
    from math import pi, sqrt, cos
    f, l = [], []
    for coord in [first, second]:
        num = findall(r'\d+', coord)
        num = [int(i) for i in num]
        
        fi = (num[2] / 3600 + num[1] / 60 + num[0]) * pi /180
        la = (num[5] / 3600 + num[4] / 60 + num[3]) * pi / 180
        if 'S' in coord:
            fi *= -1
        if 'W' in coord:
            la *= -1
        f.append(fi)
        l.append(la)
    
    fim = sum(f)/2
    dfi = f[1] - f[0]
    dla = l[1] - l[0]
    return round(R * sqrt(dfi**2 + (cos(fim) * dla)**2), 1)
print(distance("33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
'''
