VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}

def worth_of_words(words):
    max_word = ''
    max_res = 0
    for word in words:
        result = 0
        for letter in word:
            result += VALUES[letter]
        if result > max_res:
            max_res = result
            max_word = word
    return max_word
        

print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))
"""

"""               


