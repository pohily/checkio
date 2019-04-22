def boolean(x, y, operation):
    if operation == "conjunction":
        return x and y
    elif operation == "disjunction":
        return x or y
    elif operation == "implication":
        if x == True:
            return y
        else:
            return 1
    elif operation == "exclusive":
        return (x + y) % 2
    elif operation == "equivalence":
        return 1 if x == y else 0
        

print(boolean(0, 1, "equivalence"))
"""
def boolean(x, y, operation):
    if operation == "conjunction": return x and y
    elif operation == "disjunction": return x or y
    elif operation == "implication": return not x or y
    elif operation == "exclusive": return (x and not y) or (not x and y)
    elif operation == "equivalence": return not ((x and not y) or (not x and y))




def boolean(x,y,operation):
    if operation == "conjunction":
        return x&y
    elif operation == "disjunction":
        return x|y
    elif operation == "implication":
        return (not x) or y
    elif operation == "exclusive":
        return x^y
    elif operation == "equivalence":
        return x==y
"""               



