def checkio(text):
    exceptions = ['.', ':', '!', '?', '@', '$', '%']
    # split text on dates, times, and words

    from re import findall, split, search

    result = []     # found dates and times
    points = []     # start/end of results
    chunks = []     # result of splitting text

    result += findall(r'\d\d\.\d\d\.\d\d\d\d', text)
    result += findall(r'\d\d:\d\d', text)
    for i in result:
        tmp = search(i, text)
        points.append(tmp.start())
        points.append(tmp.end())
    points.append(len(text))
    start = 0
    for point in points:
        end = point
        chunks.append(text[start:end])
        start = point
    
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
print(checkio("10011011101001110001111010001100001110010111011001000000101000011011111101000110100111011001111001100000004.01.1978"))
    

