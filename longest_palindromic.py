def longest_palindromic(text):
    text_rev = text[::-1]
    result = ''
    for start in range(len(text)):
        for end in range(1, len(text) - start+1):
            check = text[start:end]
            check_1 = text[start:end-1]
            if check not in text_rev:
                if len(check_1) > len(result):
                    if check_1 == check_1[::-1]:
                        result = check_1
                    break
                else:
                    break
            else:
                if len(check) > len(result):
                    if check == check[::-1]:
                        result = check
    return result
print(longest_palindromic("abacada"))
"""
def longest_palindromic(text):
    l = len(text)+1
    r = [[s for s in [text[f:f+e] for f in range(l-e)] if s==s[::-1]] for e in range(1,l)]
    r = list(filter(lambda x:len(x)>0,r))
    return r[-1][0]
    """


