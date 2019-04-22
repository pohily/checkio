exceptions = ['.', ':', '!', '?', '@', '$', '%']
class HackerLanguage:
    def __init__(self):
        self.text = ''

    def write(self, text):
        self.text += text

    def delete(self, N):
        self.text = self.text[ :len(self.text) - N]

    def prepare(self):
        # split text on dates, times, and words
        from re import findall, split, search

        result = []     # found dates and times
        points = []     # start/end of results
        chunks = []     # result of splitting text

        result += findall(r'\d\d\.\d\d\.\d\d\d\d', self.text)
        result += findall(r'\d\d:\d\d', self.text)
        for i in result:
            tmp = search(i, self.text)
            points.append(tmp.start())
            points.append(tmp.end())
        points.append(len(self.text))
        start = 0
        for point in points:
            end = point
            chunks.append(self.text[start:end])
            start = point
        return (chunks, result)

    def send(self):
        # encode text
        chunks, result = self.prepare()
        encode = []
        for chunk in chunks:
            if chunk in result:
                encode.append(chunk)
            else:
                for letter in chunk:
                    if letter in exceptions:
                        encode.append(letter)
                    elif letter == ' ':
                        encode.append('1000000')
                    else:
                        encode.append(bin(ord(letter))[2:])
        return ''.join(encode)

    def read(self, text):
        # decode text
        self.text = text
        chunks, result = self.prepare()
        decode = []
        for chunk in chunks:
            if chunk in result:
                decode.append(chunk)
            else:
                while chunk:
                    if chunk[0] in exceptions:
                        decode.append(chunk[0])
                        chunk = chunk[1:]
                    else:
                        tmp = chunk[:7]
                        chunk = chunk[7:]
                        if tmp == '1000000':
                            decode.append(' ')
                        else:
                            decode.append(chr(int(tmp, 2)))
                
        return ''.join(decode)
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()
    message_3 = HackerLanguage()
    message_4 = HackerLanguage()
    message_3.write("Michael Pohily 04.01.1978")
    print(message_3.send())
    assert message_1.send() == "111001111001011100011111001011001011110100"
    print(message_2.read("11001011101101110000111010011101100"))
    print(message_4.read("10011011101001110001111010001100001110010111011001000000101000011011111101000110100111011001111001100000004.01.1978"))
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
'''


'''
