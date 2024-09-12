from collections import defaultdict
import sys
input = open('revegetate.in', 'r').readline
out = open('revegetate.out', 'w')

# out = sys.stdout

n, m = map(int, input().split())



adj = defaultdict(list)
vis = [0]*(n+1)
color = [0]*(n+1)

for _ in range(m):
    s, u, v = input().split()
    if s == 'S':
        s = 0
    else:
        s = 1
    u = int(u)
    v = int(v)
    adj[u].append([v, s])
    adj[v].append([u, s])

components = []
ans = 1
for i in range(1, n+1):
    if not vis[i]:
        components.append([i])
        stack = [i]
        vis[i] = 1
        while stack:
            v = stack.pop()
            for nn, c in adj[v]:
                if not vis[nn]:
                    vis[nn] = 1
                    stack.append(nn)
                    # print(f"from {v} to {nn}")
                    color[nn] = color[v]^c
                    components[-1].append(nn)
                elif color[nn] != color[v]^c:
                    ans = 0
# print(components)
# print(color)
if ans:
    tt = 0
    for cmp in components:
        if cmp:
            tt += 1
    print(bin(2**tt)[2:], file=out)
else:
    print(0, file=out)