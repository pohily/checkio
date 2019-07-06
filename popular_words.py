def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.lower()
    result = {}
    for word in words:
        text1 = text
        count = 0
        while text1:
            if word not in text1:
                break
            found = text1.index(word)
            if found != 0:
                m = text1[found-1]
                if m != ' ' and m != '\n':
                    text1 = text1[(found + len(word)):]
                    continue
            text1 = text1[(found + len(word)):]
            if not text1:
                count += 1
                break
            if  text1[0] == " " or text1[0] == "\n" or text1[0] == ',' or text1[0] == '.':
                count += 1
            
            if word not in text1:
                break
        result[word] = count
    return result

print(popular_words('''
And the Raven never flitting still is sitting still is sitting
On the pallid bust of Pallas just above my chamber door
And his eyes have all the seeming of a demon’s that is dreaming
And the lamp-light o’er him streaming throws his shadow on the floor
And my soul from out that shadow that lies floating on the floor
Shall be lifted nevermore
''', ["raven","still","is","floor","nevermore"]))

