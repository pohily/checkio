def checkio(text: str) -> str:
    text = text.lower()
    set_text = sorted(list(set(text)))
    result = 0
    max_result = 0
    for letter in set_text:
        if letter.isalpha():
            m = text.count(letter)
            if m > max_result:
                max_result = m
                result = letter
    return result
    
    
print(checkio("AAaooo!!!!"))

"""

    """


