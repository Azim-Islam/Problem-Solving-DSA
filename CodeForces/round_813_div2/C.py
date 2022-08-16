import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set()
    d = [0]*n
    r = [0]*(n+1)
    for i in range(n):
        s.add(arr[i])
        d[i] = len(s)
        r[arr[i]] = i
    idx = -1
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            idx =  i-1
            break
    ans = 0
    for i in range(idx, -1, -1):
        ans = max(ans, d[r[arr[i]]])
    print(ans)