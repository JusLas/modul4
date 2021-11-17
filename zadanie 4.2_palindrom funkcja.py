def is_palindrom(word):
    return word == word[::-1]

returned = is_palindrom("potop")
print(returned)