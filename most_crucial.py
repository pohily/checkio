def most_crucial(net, users):
    nodes = set()
    # make set of nodes
    for edge in net:
        for node in edge:
            nodes.add(node)
    nodes = sorted(nodes)

    # count happiness with one node off at a time
    results = {}        # key - happiness, value - off node
    
    for off in nodes:
        happiness = users[off]
        # find subnetworks
        subs = []
        for n in nodes:
            for edge in net:
                if n in edge:
                    # check for crushes in edge
                    tmp = set()
                    for end in edge:
                        if end != off:
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
        # for every subnetwork in net find its happiness
        for sub in subs:
            tmp = 0
            for node in sub:
                tmp += users[node]
            happiness += tmp ** 2
            if not happiness in results:
                results[happiness] = [off]
            else:
                results[happiness] += [off]
        
    return results[min(results.keys())]
print(most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
'''
