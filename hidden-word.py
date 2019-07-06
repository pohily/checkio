from itertools import zip_longest
def checkio(text, word):
    text = text.lower().rstrip().split('\n')
    for i, v in enumerate(text):
        text[i] = ''.join(v.split())
        #print(text[i])
        if word in text[i]:
            return [i+1, text[i].index(word)+1, i+1, text[i].index(word)+len(word)]
    text_trans = list(zip_longest(*text, fillvalue=""))
    for i, v in enumerate(text_trans):
        text_trans[i] = ''.join(v)
        #print(text_trans[i])
        if word in text_trans[i]:
            return [text_trans[i].index(word)+1, i+1, text_trans[i].index(word)+len(word), i+1]
    return False

print(checkio("xa\nxb\nx","ab"))
                    



