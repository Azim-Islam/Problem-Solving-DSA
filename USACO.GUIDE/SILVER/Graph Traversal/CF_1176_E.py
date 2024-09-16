from collections import defaultdict
import sys

input = sys.stdin.readline
out = sys.stdout

ans = []

for _ in range(int(input())):
    n, m = map(int, input().split())
    adj = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    color = [0]*(n+1)
    vis = [0]*(n+1)
    stack = [1]
    vis[1] = 1

    while stack:
        v = stack.pop()
        for nn in adj[v]:
            if not vis[nn]:
                stack.append(nn)
                vis[nn] = 1
                color[nn] = color[v]^1

    reds = sum(color)

    if reds <= n//2:
        ans.append(reds)
        ans.append("\n")
        for i in range(1, n+1):
            if color[i]:
                ans.append(i)
                ans.append(" ")
        ans.append("\n")
    else:
        ans.append(str(n - reds))
        ans.append("\n")
        for i in range(1, n+1):
            if not color[i]:
                ans.append(i)
                ans.append(" ")
        ans.append("\n")

print("".join(map(str, ans)), file=out)
