import sys
from collections import defaultdict

input = sys.stdin.readline
out = sys.stdout

n, x = map(int, input().split())
arr = list(map(int, input().split()))

cum = [0]
count = defaultdict(int)
count[0] = 1

ans = 0
for i, v in enumerate(arr):
    cum.append(cum[-1]+v)
    t = cum[-1]-x
    ans += count[t]
    count[cum[-1]] += 1
print(ans)
    