from typing import List
def check(l):
    tmp = ''
    tmp2 = ''
    for i in range(3):
        tmp += l[i][i]
        tmp2 += l[i][2 - i]
    l.append(tmp)
    l.append(tmp2)
    for row in l:
        a = list(set(row))
        if len(a) == 1:
            if a[0] != '.':
                return a[0]
    del l[-1]
    del l[-1]
    return 'D'

def checkio(game_result: List[str]) -> str:
    if check(game_result) != 'D':
        return check(game_result)
    game_result = list(zip(*game_result))
    
    return check(game_result)



print(checkio([
        "...",
        "XXX",
        ".OO"]))

"""

    """


