def domino_chain(tiles: str) -> int:
    #find all nubers and their frequency
    numbers = []
    freq = [0]*7
    for tile in tiles:
        if tile.isdigit():
            numbers.append(tile)
            freq[int(tile)] += 1
    
    # check for doubles
    doubles = 0
    d = []
    for i in range(7):
        if f'{str(i)}-{str(i)}' in tiles:
            doubles += 1
            d.append(i)

    # check if there's no chains
    odd = 0
    for f in freq:
        if f%2 == 1:
            odd +=1

    print('odd', odd)
    print('freq', freq)
    print('doubles', doubles, d)
    if odd > 2 or odd == 1:
        return 0
    
    
    

print(domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4"))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")
'''
