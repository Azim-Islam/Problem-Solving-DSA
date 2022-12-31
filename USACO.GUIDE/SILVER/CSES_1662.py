import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)
d[0] = 1


n = int(input())
arr = list(map(int, input().split()))

ans = 0
s = 0

for i in arr:
    s += i
    t = s%n
    ans += d[t]
    d[t] += 1

print(ans)


