from math import pi, sqrt, e, asin, log
def checkio(height, width):
    height = float(height)
    width = float(width)
    if height > width:                          # prolate spheroid
        E = sqrt(1 - pow(width / 2, 2) / pow(height / 2, 2))
        volume = pow(width, 2) * height * pi / 6
        surface = 2 * pi * pow(width / 2, 2) * (1 + asin(E) * (height/2) / (width / 2 * E))
    elif height == width:                       # sphere
        volume = 4 / 3 * pi * pow(height / 2, 3)
        surface = 4 * pi * pow(height / 2, 2)
    else:                                       #  oblate spheroid
        E = sqrt(1 - pow(height / 2, 2) / pow(width / 2, 2))
        volume = pow(width, 2) * height * pi / 6
        surface = 2 * pi * pow(width / 2, 2) + pi * log((1+E)/(1-E), e) * pow(height / 2, 2) / E
    return [round(volume, 2), round(surface, 2)]


print(checkio(2, 4))
                    



