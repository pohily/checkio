def cards(deck, hand):
    every_card = []
    for card in range(1, deck+1):
        every_card += [[card-1, card]]
    found = True
    hand.sort()
    #print(every_card)
    while hand:
        if found == False:
            return False
        found = False
        check = hand[0]
        hand = hand[1:]
        for card in every_card:
            if check in card:
                every_card.remove(card)
                print(every_card)
                found = True
                break
        
    return True if found == True else False
print(cards(25,[17,11,16,12,5,12,11]))
"""

"""
