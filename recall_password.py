def recall_password(cipher_grille, ciphered_password):
    result = ''
    key = 0
    grille = cipher_grille
    while key < 4:
        
        for i, row in enumerate(cipher_grille):
            for j, letter in enumerate(row):
                if letter == 'X':
                    result += ciphered_password[i][j]
        if key%2 == 0:
            cipher_grille = list(zip(*cipher_grille))
            for i, v in enumerate(cipher_grille):
                cipher_grille[i] = v[::-1]
            key +=1
        else:
            cipher_grille = list(grille[::-1])
            for i, v in enumerate(cipher_grille):
                cipher_grille[i] = v[::-1]
            key +=1
    return result

print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))    


"""


    """


