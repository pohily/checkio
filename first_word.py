def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    second = 'start'
    for i, v in enumerate(text):
        if ord(v)== 39 or 65<= ord(v)<= 90 or 97<= ord(v)<= 122:
            first = i
            break
    t = text[first:]
    for i, v in enumerate(t):
        if v == ' ' or v == ',' or v == '.':
            second = i + first
            break
    if second == 'start':
        second = len(text)
    return text[first:second]

print(first_word('hi'))

