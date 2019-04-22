braille = {' ':0, 'a':1, ',':2, 'b':3, 'k':5, 'l':7, 'c':9, 'i':10, 'f':11, 'm':13, 's':14, 'p':15, 'e':17, '-':18, 'h':19, 'o':21, '!':22, 'r':23, 'd':25, 'j':26, 'g':27, 'n':29, 't':30, 'q':31, 'capital':32, '_':36, 'u':37, '?':38, 'v':39, 'x':45, '.':50, 'z':53, 'number':60, 'y':61, 'w':62}
number = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '0':'j'}

def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]

# add encoded letter to output
def add_letter(lttr, arr, position, cur_let, txt):
    pos = 0
    for i in range(-3, 0):
        arr[i] += lttr[pos]
        # add 0 bitween the letters
        if position != 10 and cur_let != len(txt) -1:
            arr[i] += [0]
        pos +=1
    return arr

def braille_page(text: str):
    # preprocess text
    text = list(text)
    # check letter
    text1 = []
    for letter in text:
        if letter.isdigit():
            text1.append('number')
            text1.append(number[letter])
        elif letter.isupper():
            text1.append('capital')
            text1.append(letter.lower())
        else:
            text1.append(letter)
    text = text1[:]        
    
    sign = 1            # added leters on a string
    result = []         # output text
    current_letter = 0  # current encoding letter in text
    
    while current_letter < len(text):
        
        # if new string add 3 rows in ouput text    
        if sign == 1:
            result.append([])
            result.append([])
            result.append([])
        elif sign == 11: # if there's 10 signs in string add empty row
            sign = 1
            result.append([0]*29)
            continue
        
        letter = text[current_letter]
        
        # encode a letter
        encode = convert(braille[letter])
        result = add_letter(encode, result, sign, current_letter, text)

        # increment counters
        sign += 1       
        current_letter += 1 
    # check for multilined text, and if there is, append it with zeros
    if len(result) > 3 and len(result[-1]) < 29:
        x = 29 - len(result[-1])
        pos = 0
        for i in range(-3, 0):
            result[i] += [0]*x
            pos +=1
    for i in result:
        print(i)

    return result
braille_page('Double  Space')
