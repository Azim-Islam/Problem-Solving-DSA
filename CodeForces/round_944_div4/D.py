for _ in range(int(input())):
    s = list(input())
    s = list(map(int, s))
    r = []
    r.append(s[0])
    ans = 1
    for i in range(1, len(s)):
        if s[i] != r[-1]:
            r.append(s[i])
    f = False
    for i in range(len(r)-1):
        if r[i] > r[i+1]:
            if i+1 == len(r)-1:
                ans += 1
            else:
                f = True
                ans += 2
    
    if r[0] == 1 and f:
        ans -= 1


    print(ans)