from collections import Counter


f = lambda x: abs(int(x))
for _ in range(int(input())):
    n = int(input())
    arr = list(map(f, input().split()))
    c = Counter(arr)
    tt = 0
    ans = 0
    for k in c:
        if k == 0:
            tt = 1
        else: 
            if c[k] >= 2:
                ans += 2
            else:
                ans += 1
    print(ans + tt)