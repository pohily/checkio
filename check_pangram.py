def check_pangram(text):
    abc = [chr(letter) for letter in range(97, 123)]
    text = text.lower()
    for letter in text:
        if letter in abc:
            abc.remove(letter)
    return True if abc == [] else False



print(check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"))
"""
def check_pangram(text):
    for c in list(range(97,123)):
        if chr(c) not in text.lower():
            return False
    return True
"""               



