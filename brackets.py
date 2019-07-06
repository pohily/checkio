def checkio(expression):
    stack = []
    for char in expression:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        if char == ')' or char == ']' or char == '}':
            if stack != []:
                check = stack.pop()
            else:
                return False
            if check == '(' and char == ')':
                continue
            elif check == '[' and char == ']':
                continue
            elif check == '{' and char == '}':
                continue
            else:
                return False
    if stack == []:
        return True
    else:
        return False


print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))
"""

    """


