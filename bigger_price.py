def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here
    tmp = []
    for d in data:
        tmp.append((d['price'], d))
    tmp = sorted(tmp, reverse=True)[:limit]
    
    return [b for (a, b) in tmp]

print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

