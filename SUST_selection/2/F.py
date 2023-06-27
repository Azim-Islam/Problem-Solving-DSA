from collections import defaultdict

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    pref = [0]
    s = 0
    for i in arr:
        s += i
        pref.append(s%x)

    d = defaultdict(list)
    ans = -1
    for i, v in enumerate(pref):
        if i > 0:
            d[v].append(i)
    
    for k in d:
        if k > 0:
            ans = max(ans, d[k][-1])

    if 0 in d:
        v = d[0][-1]
        for i in d[0][:-1]:
            if abs(pref[v]-pref[i-1]) > 0:
                ans = max(ans, v-i+1)


    print(ans)
