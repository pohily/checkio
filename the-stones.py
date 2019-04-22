def stones(pile, moves):
    result = ["F"] * (pile)
    result[0] = 'F'
    for i in range(pile):
        for j in moves:
            if i - j >= 0 and result[i - j] == 'F':
                result[i] = 'T'
                break
    print(result)
    return 1 if result[pile-1] == 'T' else 2
    
print(stones(17, [1, 3, 4, 6, 9]))

"""

"""
