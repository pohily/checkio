def best_stock(data):
    # your code here
    data1 = dict(zip(data.values(), data.keys()))
    
    return data1[max(data.values())]
print(best_stock({'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9}))

