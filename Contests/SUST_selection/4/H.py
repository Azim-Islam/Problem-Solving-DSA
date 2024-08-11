from collections import defaultdict

n = int(input())

visited = [0]*(n+1)

d = defaultdict(int)
m = defaultdict(list)

red = 0
blue = 0

for i in range(n-1):
    u, v = map(int, input().split())
    m[u].append(v)
    m[v].append(u)

kv = (1, 1)
stack = []
stack.append(kv)

while stack:
    t = stack.pop()
    tv = 0 if t[1] else 1
    visited[t[0]] = 1
    d[t[0]] = t[1]
    for v in m[t[0]]:
        if not visited[v]:
            stack.append((v, tv))




for k in d:
    if d[k] == 1:
        red += 1
    else:
        blue += 1

# print(d, red, blue)

print(red*blue - (n-1))
