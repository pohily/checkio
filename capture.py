def capture(matrix):
    time = 0            # current time
    stand = [0]         # computers that still stand 
    defeated = []       # already defeated
    
    while len(defeated) < len(matrix):
        
        # find defeated computers in stand, add to fresh_defeated, move to defeated
        fresh_defeated = [] 
        for computer in stand:
            if matrix[computer][computer] == 0:
                fresh_defeated.append(computer)
                defeated.append(computer)
        stand = [i for i in stand if matrix[i][i] != 0]

        # add neighbours of fresh_defeated to stand
        for computer in fresh_defeated:
            for index, candidate in enumerate(matrix[computer]):
                if candidate == 1 and index not in defeated and index not in stand:
                    stand.append(index)

        #for computer in stand decrease its protection
        for computer in stand:
            matrix[computer][computer] -= 1

        time += 1
    return time-1

capture([           [0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]])
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
