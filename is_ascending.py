def is_ascending(items: Iterable[int]) -> bool:
    return all(items[i] > items[i-1] for i in range(1, len(items)))

        
print(is_ascending([4, 5, 6, 7, 3, 7, 9]))  
"""
"""               



