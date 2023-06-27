from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

d = defaultdict(int)


for i in arr:
    d[i] += 1

for i in range(1, n+1):
    print(d[i])