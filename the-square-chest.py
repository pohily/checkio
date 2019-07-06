from typing import List

def checkio(lines_list: List[List[int]]) -> int:
    square = 0
    s = [1, 2, 3, 5, 6, 7, 9, 10, 11]
    m = [1, 2, 5, 6]
    l = [1]
    ### s
    for point in s:
        if [point, point+1] in lines_list and (
            [point, point + 4]) in lines_list and (
            [point+1, point+1 + 4]) in lines_list and (
            [point + 4, point+1 + 4]) in lines_list:
            square += 1
    ### m
    for point in m:
        if [point, point+1] in lines_list and (
        [point+1, point+1+1]) in lines_list and (

        [point, point + 4]) in lines_list and (
        [point +4, point +4+4]) in lines_list and (

        [point+1+1, point+1+1 +4]) in lines_list and (
        [point+1+1 +4, point+1+1 +4+4]) in lines_list and (

        [point +4+4, point+1 +4+4]) in lines_list and (
        [point+1 +4+4, point+1+1 +4+4]) in lines_list:
            square += 1
    ### l
    for point in l:    
        if [point, point+1] in lines_list and (
            
            [point+1, point+1+1] )in lines_list and (
            
            [point+1+1, point+1+1+1]) in lines_list and (
        
            
            [point, point +4]) in lines_list and (
            
            [point +4, point +4+4] )in lines_list and (
            
            [point +4+4, point +4+4+4]) in lines_list and (

            
            [point+1+1+1, point+1+1+1 +4]) in lines_list and (
            
            [point+1+1+1 +4, point+1+1+1 + 4+4]) in lines_list and (
            
            [point+1+1+1 +4+4, point+1+1+1 + 4+4+4]) in lines_list and (

            
            [point+4+4+4, point+1 +4+4+4]) in lines_list and (
            
            [point+1 +4+4+4, point+1+1 +4+4+4]) in lines_list and (
            
            [point+1+1 +4+4+4, point+1+1+1 +4+4+4]) in lines_list:
            square += 1
    return square

print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))    


"""

    """


