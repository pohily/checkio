def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    result = []
    for word in phrases:
        while 'right' in word:
            i = word.index('right')
            word = word[:i] + 'left' + word[i+5:]
        result.append(word)
    return ','.join(result)

print(left_join(("left", "right", "left", "stop")))

