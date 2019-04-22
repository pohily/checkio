def subnetworks(net, crushes):
    # find working nodes
    nodes = set()
    for edge in net:
        for node in edge:
            if node not in crushes:
                nodes.add(node)
    nodes = sorted(nodes)
    # find subnetworks
    subs = []
    for n in nodes:
        for edge in net:
            if n in edge:
                # check for crushes in edge
                tmp = set()
                for end in edge:
                    if end not in crushes:
                        tmp.add(end)
                # check if any node in tmp already in subnets if not add it
                if subs:
                    for sub in subs:
                        added = False
                        for end in tmp:
                            if end in sub:
                                sub |= tmp
                                added = True
                                break
                    if not added:
                        subs.append(tmp)
                else:
                    subs.append(tmp)
                

            
    print('n', nodes)
    print('s', subs)
    return len(subs)
print(subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
'''
