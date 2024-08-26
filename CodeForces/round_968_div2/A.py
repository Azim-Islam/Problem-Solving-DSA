for _ in range(int(input())):
    n = int(input())
    s = list(input())
    idx = 0
    F = True
    if s[0] == s[-1]:
        F = False

    if F: print("YES")
    else: print("NO")