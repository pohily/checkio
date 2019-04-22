def frequency_sort(items):
    unics = set(items)
    result, freq = [], []
    for u in unics:
        freq.append(items.count(u))
    freq = sorted(freq, reverse=True)
    count = 0
    for item in items:
        if items.count(item) == freq[count] and item not in result:
            for i in range(freq[count]):
                result.append(item)
            count += 1
            if count == len(freq): break
    return result


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
"""
 return sorted(items, 
                  reverse=True, 
                  key=lambda item: (items.count(item), -items.index(item))
                  


from collections import Counter
def frequency_sort(items):
    return [value for value, count in Counter(items).most_common() for _ in range(count)] 
"""               



