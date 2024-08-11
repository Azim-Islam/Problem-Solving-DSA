from collections import defaultdict

f = lambda : float('inf')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    rm = defaultdict(int)
    lf = defaultdict(f)
    for i, v in enumerate(arr):
        rm[v] = max(i, rm[v])
        lf[v] = min(i, lf[v])
    
    suffix =[0]*(n-1) + [1 if rm[arr[-1]] == n-1 else 0]
    for i in range(n-2, -1, -1):
        if rm[arr[i]] == i:
            suffix[i] = suffix[i+1] + 1
        else:
            suffix[i] = suffix[i+1]
    
    ans = 0

    for i in range(0, n):
        if lf[arr[i]] == i:
            ans += suffix[i]

    print(ans)