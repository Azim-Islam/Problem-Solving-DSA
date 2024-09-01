from collections import Counter

def check1(string):
    string = string[::]
    ans = 0
    if len(string)%2:
        ans += 1
        string.pop()
    
    mx = [0]*26
    c = 0
    for i in range(0, len(string), 2):
        mx[ord(string[i]) - 97] += 1 
        c += 1
    mx.sort()
    ans += c - mx[-1]

    mx = [0]*26
    c = 0
    for i in range(1, len(string), 2):
        mx[ord(string[i]) - 97] += 1 
        c += 1
    mx.sort()
    ans += c - mx[-1]

    return ans

def check(string):
    string = string[::]
    ans = 0
    if len(string)%2:
        ans += 1
        freq = Counter(string)
        to_del = ''
        mn = float('inf')
        for k in freq:
            if freq[k] <= mn:
                to_del = k
                mn = freq[k]
        string.remove(to_del)
    
    mx = [0]*26
    c = 0
    for i in range(0, len(string), 2):
        mx[ord(string[i]) - 97] += 1 
        c += 1
    mx.sort()
    ans += c - mx[-1]

    mx = [0]*26
    c = 0
    for i in range(1, len(string), 2):
        mx[ord(string[i]) - 97] += 1 
        c += 1
    mx.sort()
    ans += c - mx[-1]

    return ans
    

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    print(min(check(s), check(s[::-1])), check1(s))