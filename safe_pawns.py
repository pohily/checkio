def safe_pawns(pawns: set) -> int:
    pawns_indexes = [[],[],[],[],[],[],[],[]]
    for p in pawns:
        row = int(p[1]) -1
        col = ord(p[0]) - 97
        pawns_indexes[row].append(col)
    ## row 0
    unsafe = len(pawns_indexes[0])
    ## rows 1-7
    for row in range(1, 8):
        if pawns_indexes[row] != []:
            for pawn in pawns_indexes[row]:
                if pawn-1 not in pawns_indexes[row-1] and pawn+1 not in pawns_indexes[row-1]:
                    unsafe += 1
    return len(pawns) - unsafe
print(safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}))

"""

    """


