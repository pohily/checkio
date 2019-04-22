def checkio(required, operations):
    #if first one is enough - return it
    if required <= operations[0][1] - operations[0][0] + 1:
        return 1
    
    op_num = 1               # current operation number
    done = [operations[0]]   # done operations list
    result = 1               # requiered number of operations
    while op_num < len(operations):
        #check if current operation is overlapped with any ops in done list
        current = operations[op_num]
        
        op_num += 1          # increment counters
        result += 1
        tmp = done[:]
        for op in done:
            if current [0] < op[0] and current[1] < op[1] and current[1] >= op[0]:
                tmp.remove(op)
                current = [current[0], op[1]]
            elif current[0] > op[0] and current[0] <= op[1] and current[1] > op[1]:
                tmp.remove(op)
                current = [op[0], current[1]]
            elif current[0] <= op[0] < current[1] and current[0] < op[1] <= current[1]:
                tmp.remove(op)
            elif op[0] <= current[0] < op[1] and op[0] < current[1] <= op[1]:
                tmp.remove(op)
                current = op
        done = tmp[:]
        done.append(current)

        # check if operations in done list is enough
        lenths = []
        for op in done:
            lenths.append(op[1] - op[0] + 1)
        print('num', result)
        print('done', done)
        print('lenths', lenths)
        if sum(lenths) >= required:
            return result
    return -1


print(checkio(15,[[1,2],[20,30],[25,28],[5,10],[4,21],[1,6]]))    
"""assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"

"""





