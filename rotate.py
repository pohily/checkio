def rotate(state, pipe_numbers):
    pipe_numbers = sorted(set(pipe_numbers))
    result = []
    for i in range(len(state)):
        ok = True
        for number in pipe_numbers:
            if state[(i + number) % len(state)] != 1:
                ok = False
        if ok == True:
            result.append((len(state) - i)% len(state))
    return sorted(result)

        
print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]))
"""

"""               



