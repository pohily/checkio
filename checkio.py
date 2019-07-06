def checkio(*args):
    
    
    if len(args) < 2:
        return 0
    
    result = max(args) - min(args)
    
    return round(result, 4)

print(checkio(10.2, -2.2, 0, 1.1, 0.5))

