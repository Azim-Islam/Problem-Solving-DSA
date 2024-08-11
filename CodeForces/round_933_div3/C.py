

def check(a, b, c):
    if a == "m" and b == "a" and c == "p":
        return 1
    if a == "p" and b == "i" and c == "e":
        return 1
    return 0

def check_mapie(a, b, c, d , e):
    if a == "m" and b == "a" and c == "p" and d == "i" and e == "e":
        return 1
    return 0

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    if n <= 2: print(0)
    else:
        ans = 0
        count = 0
        for i in range(0, n-2):
            if check(s[i], s[i+1], s[i+2]):
                ans += 1
        for i in range(0, n-4):
            if check_mapie(s[i], s[i+1], s[i+2], s[i+3], s[i+4]):
                count += 1
        print(ans - count)