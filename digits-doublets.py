"""def checkio(numbers):
    numbers = [str(i) for i in numbers]
    pos_change = {}                          # make graph of possible changes
    for first in numbers:
        for second in numbers:
            if first != second:
                if first[0] == second[0] and first[1] == second[1]:
                    if first not in pos_change:
                        pos_change[first] = [second]
                    else:
                        pos_change[first] += [second]
                elif first[0] == second[0] and first[2] == second[2]:
                    if first not in pos_change:
                        pos_change[first] = [second]
                    else:
                        pos_change[first] += [second]
                elif first[1] == second[1] and first[2] == second[2]:
                    if first not in pos_change:
                        pos_change[first] = [second]
                    else:
                        pos_change[first] += [second]
                                        
                                            # find shortest path
    
    def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
     
    path = find_shortest_path(pos_change, numbers[0], numbers[-1])
    return [int(i) for i in path]
print(checkio([456, 455, 454, 356, 656, 654]))
"""
from collections import deque

def checkio(numbers):
    q = deque([[numbers[0]]])
    while q:
        chain = q.popleft()
        if chain[-1] == numbers[-1]:
            return chain
        for n in numbers:
            if connected(chain[-1], n):
                q.append(chain + [n])
    return []
    
def connected(a, b):
    return [(a//100)-(b//100), ((a%100)//10)-((b%100)//10), (a%10)-(b%10)].count(0) == 2

print(checkio([456, 455, 454, 356, 656, 654]))                  



