def checkio(f,g):

    # Replace with your code
    def h(*args,**kwargs):
        a = a1 = a2 = b = b1 = b2 = ''
        try:
            a1 = f(*args,**kwargs)
            #print('a1', a1)
        except Exception as a:
             if a:
                 a2 = a
        try:
            b1 = g(*args,**kwargs)
            #print('b1', b1)
        except Exception as b:
            if b:
                b2 = b
        if a1 != None and a2 == '':
            result = a1
        elif b1 != None and b2 == '':
            result = b1
        else:
            result = None

        if a1 == b1 and a2 == '' and b2 == '':
            status = 'same'
        elif a1 != b1 and a2 == '' and b2 == '':
            status = 'different'
        elif (a1 == None or a2 != '') and (b1 != None and b2 == ''):
            status = 'f_error'
        elif (b1 == None or b2 != '') and (a1 != None and a2 == ''):
            status = 'g_error'
        elif (a1 == None or a2 != '') and (b1 == None or b2 != ''):
            status = 'both_error'
        print(result, status)
        return (result, status)
    return h

if __name__ == '__main__':
       
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    # (x+y)(x-y)/(x-y)
    print(checkio(f = lambda x: abs(x)\ndef g(x):\n  if x>0:\n    return x\n  elif x<0:\n    return -x\nc = checkio(f,g)\nresult = c(0)\n))
