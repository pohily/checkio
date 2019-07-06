def two_teams(sailors):
    boats = [[], []]
    for sailor in sailors:
        if 20 <= sailors[sailor] <= 40:
            boats[1].append(sailor)
        else:
            boats[0].append(sailor)
        boats[0].sort()
        boats[1].sort()
    return boats

print(two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}))

