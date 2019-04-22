from typing import List
def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    result = []
    for r in range(rows):
        if r % 2 == 1:
            c = list(reversed(range(start, start+cols)))
            start += cols
            result.append(c)
        else:
            c = list(range(start, start+cols))
            start += cols
            result.append(c)
    return result
        
print(create_zigzag(3, 3, 5))  
"""
"""               



