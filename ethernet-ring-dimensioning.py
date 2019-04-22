from math import ceil
ETHERNET = (100, 40, 10, 1, 0.1) # Ethernet bandwidth capacity in Gbps

def makepath(str):
    path = []
    if len(str)>2:
        path.append(str[0] + str[-1])
    for i in range(1, len(str)):
        path.append(str[i-1] + str[i])
    return path

def checkio(ring, *flows):
    # make a dict of edges
    edges = {}
    for i in makepath(ring):
        edges[i] = 0
    
    # for every flow find shortest path and add its width in the edges dict
    for flow in flows:
        change = False
        start = ring.index(flow[0][0])
        end = ring.index(flow[0][1])
        if start > end:
            start, end = end, start
            change = True
        lenth = end - start
        if lenth < len(ring)//2:
            path = makepath(ring[start:end+1])
        elif lenth == len(ring)//2 and change == True:
            path = makepath(ring[:start+1] + ring[end:])
        elif lenth == len(ring)//2 and change == False:
            path = makepath(ring[start:end+1])
        else:
            path = makepath(ring[:start+1] + ring[end:])
        print('path', path)
        for edge in path:
            if edge in edges:
                edges[edge] += flow[1]
        
        print(edges)    

    # count which capacity is enough for every edge
    capacity = edges.values()
    capacity = [i for i in capacity if i>0]
    result = [0]*5
    print(sorted(capacity, reverse=True))
    for i, v in enumerate(ETHERNET[::-1]):
        result[i] += sum([1 for flow in capacity if flow <= v])
        capacity = [i for i in capacity if i > v]
        #print('cap/v', capacity, v)
    result = result[::-1]
    # check for big values
    for i in capacity:
        if i > 100:
            result[0] += ceil(i / 100)

    return result

print(checkio("ADBC",["AD",1],["DB",9],["BC",0.345],["CA",13]))
'''
if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
'''


'''
def checkio(ring, *flows):
   
    def path(ring, ingress, egress):
        ind = ring.index(ingress)
        ring = ring[ind:] + ring[:ind]
        return ring[:ring.index(egress) + 1]

    def route_indices(ingress, egress):
        cw_path = path(ring, ingress, egress)
        ccw_path = path(ring[::-1], ingress, egress)
        if len(cw_path) <= len(ccw_path):
            return (ring.index(c) for c in cw_path[:-1])
        else:
            return (ring.index(c) for c in ccw_path[:0:-1])

    traffic = [0.0] * len(ring)    
    for nodes, flow in flows:
        for i in route_indices(nodes[0], nodes[1]):
            traffic[i] += flow

    links = [0] * len(ETHERNET)
    for flow in traffic:
        link = min((e for e in ETHERNET if e >= flow), default= ETHERNET[0])
        while flow > 0:
            flow -= link
            links[ETHERNET.index(link)] += 1
    return links
'''