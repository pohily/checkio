def is_stressful(subj):
    """
        recoognise stressful subject
    """
    """### 1
    if subj[-3:] == '!!!':
        return True
    
    ### 2
    upper = True
    for elem in subj:
        if ord(elem)== 33 or ord(elem) == 63 or ord(elem) == 32 or ord(elem) == 44 or ord(elem) == 46 or ord(elem) == 45:
            continue
        if (65 > ord(elem) or ord(elem) > 90):
            upper = False
    if upper == True:
        return True"""

    ### 3
    subj = subj.lower()
    red = ["help", "asap", "urgent"]
    for word in red:
        if word in subj:
            return True

    for word in red:
        test_subj = subj.split()
        
        for test in test_subj:
            is_in = True
            for letter in word:
            
                if letter in test:
                
                    test = test[test.index(letter)+1:] 
                else:
                    is_in = False
                    break
            if is_in == True:
                return True
    return False   

print(is_stressful("UUUURGGGEEEEENT here"))
