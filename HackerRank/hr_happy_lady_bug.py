
from collections import Counter
def checkString(string, n):
    if n == 1:
        return True
    if n>1 and (string[0] != string[1]):
        return True
    if n>1 and string[n-1] != string[n-2]:
        return True
    for i in range(1, n-1):
            if  string[i+1] != string[i] and string[i-1] != string[i]:
                return True
    return False
def happy(string, n):
    dict_a = Counter(string)

    if dict_a["_"] == 0:
        if checkString(string, n):
            return False
        else:
            return True
    else:
        for i,j in dict_a.items():
            if i != "_" and j == 1:
                return False
        else:
            return True
    
for _ in range(int(input())):
    n = int(input())
    string = list(input())
    if happy(string, n):
        print("YES")
    else:
        print("NO")