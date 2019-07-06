def to_encrypt(text, delta):
    result = ''
    for letter in text:
        if letter == ' ':
            result += ' '
        else:
            if delta >= 0:
                m = ord(letter) + delta % 26
                if m < 123:
                    result += chr(m)
                else:
                    result += chr(m - 26)
            else:
                m = ord(letter) - (- delta) % 26
                if m < 97:
                    result += chr(26 + m)
                else:
                    result += chr(m)
    return result
    
print(to_encrypt("state secret", -13))

"""

    """


