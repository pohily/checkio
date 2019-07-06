from itertools import permutations
def make_digit(must, option):
    digit_templates = {('b', 'c'):1, ('a', 'b', 'd', 'e', 'g'):2, ('a', 'b', 'c', 'd', 'g'):3, ('b', 'c', 'f', 'g'):4, ('a',  'c', 'd', 'f','g'):5, ('a', 'c', 'd', 'e', 'f', 'g'):6, ('a', 'b', 'c'):7, ('a', 'b', 'c', 'd', 'e', 'f', 'g'):8, ('a', 'b', 'c', 'd', 'f', 'g'):9, ('a','b', 'c', 'd', 'e', 'f'):0}
    opt_perm, digits, result  = [], [], []

    for i in range(len(option)+1):         #make permutation of optional digits
        opt_perm += list(permutations(option, i))
    must_list = [m.lower() for m in must]    #list of permutation of all digits
    
    for o in opt_perm:
        digits.append(tuple(sorted(set(must_list + list(o)))))
    for dig in digits:             #find real digit we can make of our segments
        if dig in digit_templates:
            result.append(digit_templates[dig])
    return sorted(set(result))


def sort_seg(arr):                   #sort segments for first and second digits
    first = []
    second = []
    for d in arr:
        if d.isupper():
            first.append(d.lower())
        else:
            second.append(d)
    return first, second


def seven_segment(lit_seg, broken_seg):
    f_l, s_l = sort_seg(lit_seg)
    f_b, s_b = sort_seg(broken_seg)
        
    first_digit = make_digit(f_l, f_b)
    second_digit = make_digit(s_l, s_b)
    
    print('first_digit, second_digit', first_digit, second_digit)
    return len(first_digit) * len(second_digit)

print(seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}))
                    



