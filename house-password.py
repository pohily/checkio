def checkio(data: str) -> bool:
    if len(data)<10: 
        return False
    digit = False
    lower = False
    upper = False
    for letter in data:
        if letter.isdigit():
            digit = True
        elif letter.islower():
            lower = True
        elif letter.isupper():
            upper = True
    if digit ==True and lower == True and upper == True:
        return True
    else:
        return False
    
    
print(checkio('A1213pokl'))

"""
def checkio(data):

    #replace this for solution
    if not isinstance(data,str):
        return False
    if len(data) < 10 :
        return False
    import re
    rgx1=re.compile(r'[0-9a-zA-Z]+')
    rgx2=re.compile(r'.*[0-9].*')
    rgx3=re.compile(r'.*[a-z].*')
    rgx4=re.compile(r'.*[A-Z].*')
    if not rgx1.match(data):
        return False
    if not rgx2.match(data):
        return False
    if not rgx3.match(data):
        return False
    if not rgx4.match(data):
        return False
    
    return True
   


    def checkio(d: str) -> bool:
        return len(d) >= 10 and d not in [d.lower(), d.upper()] and any(c.isdigit() for c in d)
    


    def checkio(data: str) -> bool:
    import re
    if len(data) >= 10:
        if re.search(r'[A-Z]+',data):
            if re.search(r'[a-z]+', data):
                if re.search(r'[0-9]+', data):
                    return True
    return False
    """


