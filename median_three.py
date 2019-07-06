from typing import Iterable
def median_three(els: Iterable[int]) -> Iterable[int]:
    if len(els) <= 2: return els
    result = els[:2]
    for i in range(len(els[2:])):
        result.append(sorted(els[i:i+3])[1])
    return result

print(median_three([5,2,9,1,7,4,6,3,8]))    
"""
return [sorted(els[i-2:i+1])[1] if i > 1 else n for i, n in enumerate(els)]
"""               



