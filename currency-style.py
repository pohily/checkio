def checkio(text):
    import re
    result, cents = '', True
    while True:
        # check euro style with cents
        result = re.search(r'\$.+\,\d\d\b', text)
        if not result:
            # check no cents case
            result = re.search(r'\$.+\d+\.\d\d\d\b', text)
            cents = False
            if not result:
                break
        euro = text[result.start():result.end()]
        euro = euro.replace('.', ',')
        if cents:
            euro = euro[:-3] + '.' + euro[-2:]
        text = text[:result.start()] + euro + text[result.end():]
    return text

print(checkio("$1.234.567,89"))

"""

"""               



