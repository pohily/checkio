def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
def draw(segments):
    # make graph of arcs
    gr = {}
    for s1 in segments:
        for s2 in segments:
            if s1 != s2 and (s1[0] == s2[0] and s1[1] == s2[1]) or (s1[0] == s2[2] and s1[1] == s2[3]):
                if s1 not in gr:
                    gr[s1] = {s2}
                else:
                    gr[s1].add(s2)
                if s2 not in gr:
                    gr[s2] = {s1}
                else:
                    gr[s2].add(s1)
    ss = []
    for key, value in gr.items():
        value = list(value)
        if len(value) == 1:
            ss.append(key)
        if len(value) > 1:
            begin = value[0]
            stop = value[1]
    if len(ss) == 2:
        return find_all_paths(gr, ss[0], ss[1])
    else:
        return find_all_paths(gr, begin, stop)

        
#print(draw({(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}))    
print(draw({(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),(7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}))  
"""
"""               



