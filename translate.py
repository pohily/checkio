VOWELS = "aeiouy"

def translate(phrase):
    result = ''
    while phrase:
        for letter in phrase:
            if letter == ' ':
                result += letter
                phrase = phrase[1:]
                break
            elif letter not in VOWELS:
                result += letter
                phrase = phrase[2:]
                break
            else:
                result += letter
                phrase = phrase[3:]
                break
    return result

print(translate("hieeelalaooo"))    


"""


    """


