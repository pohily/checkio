def get_cookie(cookie, name):
    from re import findall, split, search
    result = search(name, cookie)
    
    cookie = cookie[result.end()+1:]
    end = search(';', cookie)
    
    if not end:
        end = len(cookie)
    else:
        end = end.end()-1
    return cookie[:end]
print(get_cookie('theme=light; sessionToken=abc123', 'theme'))
print(get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo'))
'''


'''
