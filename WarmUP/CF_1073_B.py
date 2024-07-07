from collections import defaultdict, deque
import enum


n = int(input())

d = defaultdict(int)


arr = deque(map(int, input().split()))
brr = list(map(int, input().split()))

for i, v in enumerate(arr):
    d[v] = i+1

ans = 0
for b in brr:
    if d[b]:
        t = d[b] - ans
        print(t, end=' ')
        ans += t
        for _ in range(t):
            v = arr.popleft()
            d[v] = 0
    else: print(0, end=' ')

