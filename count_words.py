def count_words(text: str, words: set) -> int:
    result = 0
    text = text.lower()
    for word in words:
        if word in text:
            result +=1
    return result
    
print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))

"""
def count_words(text: str, words: set) -> int:
    
    return sum([1 for word in words if text.lower().find(word) >= 0])
    """


