RANKS = "23456789TJQKA"
SUITS = "scdh"
RANKS = RANKS[::-1]
SUITS = SUITS[::-1]
def sort_hand(hnd):
    result = []
    for rank in RANKS:
        for card in hnd:
            if card[0] == rank:
                result.append(card)
    return ','.join(result)

def texas_referee(cards_str):
    # make lists of nominals and suits
    nominals = []           #nominals of cards in hand 
    suits = []              #suites of cards in hand
    sort_suits = [0]*4      #number of each suit in hand
    sort_noms = [0]*13      #number of each nominal in hand
    hand = list(cards_str.split(','))
    for card in cards_str:
        if card == ',':
            continue
        elif card.isupper():
            nominals.append(card)
            sort_noms[RANKS.index(card)] += 1
            continue
        elif card.isdigit():
            nominals.append(card)
            sort_noms[RANKS.index(card)] += 1
            continue
        elif card.islower():
            suits.append(card)
            sort_suits[SUITS.index(card)] += 1
            continue
    
    # find flush
    flush = False
    max_suits = max(sort_suits)
    if max_suits > 4:
        flush = True
        for s in SUITS:
            if suits.count(s) == max_suits:
                flush_suit = s
                break
    
    # find 4
    fours = False
    if 4 in sort_noms:
        fours = True

    # find 3
    three = False
    if 3 in sort_noms:
        three = True

    # find 2
    pair = False
    if 2 in sort_noms:
        pair = True

    # sort a hand
    tmp_nom, tmp_suit, tmp_hand = [], [], []
    for rank in RANKS:
        while rank in nominals:
            i = nominals.index(rank)
            tmp_nom.append(nominals.pop(i))
            tmp_suit.append(suits.pop(i))
            tmp_hand.append(hand.pop(i))
    nominals = tmp_nom[:]
    suits = tmp_suit[:]
    hand = tmp_hand[:]
        
    # sort 3 by suits
    if three == True:
        start = nominals.index(RANKS[sort_noms.index(3)])
        y = sort_noms.count(3)
        for i in range(y):
            end = start + 3
            x1 = [] 
            x2 = []
            for suit in SUITS:
                if suit in suits[start:end]:
                    x1 += [f'{nominals[start]}{suit}']
                    x2 += [suit]
            hand = hand[:start] + x1 + hand[end:]
            suits = suits[:start] + x2 + suits[end:]
            try:
                start = nominals[end:].index(RANKS[sort_noms.index(3)])
            except ValueError:
                pass
    # sort 2 by suits
    if pair == True:
        start = nominals.index(RANKS[sort_noms.index(2)])
        y = sort_noms.count(2)
        for i in range(y):
            end = start + 2
            x1 = [] 
            x2 = []
            for suit in SUITS:
                if suit in suits[start:end]:
                    x1 += [f'{nominals[start]}{suit}']
                    x2 += [suit]
            hand = hand[:start] + x1 + hand[end:]
            suits = suits[:start] + x2 + suits[end:]
            try:
                start = nominals[end:].index(RANKS[sort_noms.index(2)])
            except ValueError:
                pass
    
    # find straight
    st = False
    cont = 0
    if sort_noms[0] > 0 and 0 not in sort_noms[9:]: # str. from A to 4
        st = True
    st_start_ranks = 0
    for i, nom in enumerate(sort_noms):
        if nom > 0:
            if not st_start_ranks:
                st_start_ranks = i 
            cont += 1
            if cont == 5:
                st = True
                break
        elif nom == 0:
            cont = 0
            st_start_ranks = 0
            
    print('nominals', nominals)
    print('suits', suits)
    print('hand', hand)
    print('sort_noms', sort_noms)
    print('sort_suits', sort_suits)
    print('st', st)
    print('fl', flush)
    print('st_start_ranks', st_start_ranks)
    
    
    # royal
    if flush == True and st == True and st_start_ranks == 0:
        result = []
        for i in RANKS[:5]:
            if suits[nominals.index(i)] != flush_suit:
                ok = False
                break
            else:
                result.append(hand[nominals.index(i)])
        if ok == True
            print('Royal')
            return ','.join(result)

    # st fl
    if flush == True and st == True:
        if sort_noms[0] > 0 and 0 not in sort_noms[9:]:
            if suits[:5] == [flush_suit]*5:
                print('St.Fl')
                return ','.join(hand[:5])
        elif flush == True and st == True and st_start_ranks != 0:
            result = []
            for i in RANKS[st_start_ranks:st_start_ranks+5]:
                if suits[nominals.index(i)] != flush_suit:
                    ok = False
                    break
                else:
                    result.append(hand[nominals.index(i)])
        if ok == True
            print('St.Fl')
            return ','.join(result)

    # four
    if fours == True:
        four = RANKS[sort_noms.index(4)]
        for i, card in enumerate(nominals):
            if card != four:
                high_card = hand[i]
                break
        print('four')
        f = f'{four}h, {four}d, {four}c, {four}s, {high_card}' 
        return sort_hand(list(f.split(',')))
    
    # full
    if three == True and pair == True:
        start = nominals.index(RANKS[sort_noms.index(3)])
        t = hand[start:start+3]
        start = nominals.index(RANKS[sort_noms.index(2)])
        p = hand[start:start+2]
        print('full')
        return ','.join(t+p)
    if sort_noms.count(3) == 2:
        start = nominals.index(RANKS[sort_noms.index(3)])
        t = hand[start:start+3]
        start = nominals[start+3:].index(RANKS[sort_noms.index(3)])
        p = hand[start:start+2]
        print('full')
        return ','.join(t+p)
    
    # fl
    result = []
    if flush == True:
        for i, s in enumerate(suits):
            if suits.count(s) == max_suits:
                result.append(hand[i])
        print('flush')
        return ','.join(result)

    # st
    if st == True:
        if sort_noms[0] > 0 and 0 not in sort_noms[9:]:
            print('str')
            return ''.join(hand[9:] + [hand[0]])
        else:
            result = []
            for i in RANKS[st_start_ranks:st_start_ranks+5]:
                result.append(hand[nominals.index(i)])
            print('str')
            return ','.join(result)

    # three
    if three == True:
        start = nominals.index(RANKS[sort_noms.index(3)])
        t = hand[start:start+3]
        t1 = nominals[start:start+3]
        high_card = []
        for j in range(2):
            for i, card in enumerate(nominals):
                if card not in t1 and hand[i] not in high_card:
                    high_card.append(hand[i])
                    break
        print('3')
        return sort_hand(t+high_card)
        

    # two pairs
    if pair == True and sort_noms.count(2) > 1:
        pair_start = sort_noms.index(2)
        start = nominals.index(RANKS[pair_start])
        p1 = hand[start:start+2]
        start = nominals.index(RANKS[pair_start+1 + sort_noms[pair_start+1:].index(2)])
        p2 = hand[start:start+2]
        for i, card in enumerate(nominals):
            if card != p1[0][0] and card != p2[0][0]:
                high_card = [hand[i]]
                break
        print('2+2')
        return sort_hand(p1 + p2 + high_card)

    # pair
    if pair == True:
        start = nominals.index(RANKS[sort_noms.index(2)])
        p = hand[start:start+2]
        high_card = []
        for j in range(3):
            for i, card in enumerate(nominals):
                if card != p[0] and hand[i] not in high_card:
                    high_card.append(hand[i])
                    break
        print('2')
        return sort_hand(p + high_card)
    
    # high card
    print('no game')
    return ','.join(hand[:5])

print(texas_referee("5c,7h,7d,9s,9c,8h,6d"))
'''
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th", "High Straight Flush"
    assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
    assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
    assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
    assert texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td", "Full House vs Flush"
    assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
    assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
    assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
    assert texas_referee("2c,3s,4s,5s,7s,2d,7h") == "7h,7s,5s,2d,2c", "Two Pairs"
    assert texas_referee("2s,3s,4s,5s,2d,7h,8h") == "8h,7h,5s,2d,2s", "One Pair"
    assert texas_referee("3h,4h,Th,6s,Ad,Jc,2h") == "Ad,Jc,Th,6s,4h", "High Cards"
'''
