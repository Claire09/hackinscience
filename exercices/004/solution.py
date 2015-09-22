import string
letters = string.ascii_lowercase[::-1]
letters = letters.replace("a", "A")
letters = letters.replace("e", "E")
letters = letters.replace("i", "I")
letters = letters.replace("o", "O")
letters = letters.replace("u", "U")
print(letters)
