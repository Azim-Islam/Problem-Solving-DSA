n = int(input())

def check(word, v):
    if len(v) == 5 and len(word) == 5:
        return True
    if len(v) == 3:
        count = 0
        for i in range(3):
            if v[i] == word[i]:
                count += 1

        if count >= 2:
            return True
    return False

for i in range(n):
    v = input()
    if check("one", v):
        print(1)
    elif check("two", v):
        print(2)
    elif check("three", v):
        print(3)