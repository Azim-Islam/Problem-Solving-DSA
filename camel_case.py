from string import ascii_uppercase
uppercases = set(ascii_uppercase)
string = input()
words = 1
for ch in string:
    if ch in uppercases:
        words += 1
print(words)