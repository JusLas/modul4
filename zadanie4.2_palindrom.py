word = "ziemniak"
if word == word[::-1]:
    print("palindrom")
else:
    print("nie jest palindromem")

word="kajak"
if word == word[::-1]:
    print("palindrom")
else:
    print("nie jest palindromem")

def is_palindrom(word):
    return word == word[::-1]

returned = is_palindrom("potop")
print(returned)