#from typing import List, Tuple
from itertools import permutations
def rotate(arr, h):
    return [h - i for i in arr][::-1]

def broken_window(pieces):# List[List[int]]) -> Tuple[List[int], List[int]]:
    if len(pieces) == 2:
        if pieces[0] == rotate(pieces[1], max(pieces[1])):
            return ([1], [0])
    height = max([max(i) for i in pieces])
    lens = [len(i) for i in pieces]
    width = sum(lens) / 2 - 1
    #rotated = [rotate(i, height) for i in pieces]
    
    # for each piece try to make chain of pieces with our width and look if   # there's a chain in the rest of pieces that correspond with it
    for index, piece in enumerate(pieces):
        w = len(piece)
        used = [piece[:]] # all used pieces with current piece
        down = [index]    # index of used pieces in down part of window
        runs = [piece[:]] # list of chain candidates
        while True:
            for ind, another_piece in enumerate(pieces):
                if another_piece not in used and len(another_piece) + len(runs[-1]) <= width+1 and runs[-1][-1] == another_piece[0]:
                    runs[-1] += another_piece[1:]
                    down.append(ind)
                    used.append(another_piece)
                    if len(runs[-1]) < width:
                        continue
                if len(runs[-1]) == width:
                    # check if there's a chain in the rest of pieces that correspond with it. If not, make another run
                    to_check = rotate(runs[-1], height)
                    rest = [i for i in pieces if i not in used]
                    for r in permutations(rest):
                        begin = r[0]
                        up = [pieces.index(begin)]
                        for i in r[1:]:
                            if i[0] == begin[-1]:
                                begin += i[1:]
                                up.append(pieces.index(i))
                        if begin == to_check:
                            
                            return (up[::-1], down)
                                
            break
                    


print(broken_window([[0, 3, 4, 1], [4, 0], [3, 0], [0, 1, 4, 0]]))
