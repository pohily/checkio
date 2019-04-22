def checkio(pattern, image):
    for ver in range(len(image) - len(pattern) + 1):
        for hor in range(len(image[0]) - len(pattern[0]) + 1):
            ok = True

            # check if pattern in current position of image
            for vp in range(len(pattern)):
                for hp in range(len(pattern[0])):
                    if image[ver + vp][hor + hp] != pattern[vp][hp]:
                        ok = False
                if ok == False:
                    break

            # if pattern is here then we mark it
            if ok == True:
                for vp in range(len(pattern)):
                    for hp in range(len(pattern[0])):
                        image[ver + vp][hor + hp] += 2
    return image





        
print(checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))  
"""

"""               



