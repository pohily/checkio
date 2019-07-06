def is_family(tree):
    start = tree[0][0]
    sons = []
    fathers = []
    for line in tree:
        sons.append(line[1])
        fathers.append(line[0])
    if len(set(sons)) != len(sons):                     #sons are unic
        return False
    for index, line in enumerate(tree):
        if line[0] != start and line[0] not in sons: 
            return False                                # stranger in family
        if line[0] != start and sons.index(line[0]) >= index:
            return False                                # first son then father
        if line[1] in fathers and fathers.index(line[1]) < index:
            return False                                #if son is dad of his dad
    return True

print(is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Logan"]]))    
assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
print("Looks like you know everything. It is time for 'Check'!")

"""

    """


