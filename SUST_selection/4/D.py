from collections import defaultdict

n, mn = map(int, input().split())
arr = [0]+list(map(int, input().split()))

m = defaultdict(list)

for i in range(mn):
    u, v = map(int, input().split())
    m[u].append(v)
    m[v].append(u)

ans = 0
visited = [0]*(n+1)

for i in range(1, n+1):
    if not visited[i]:
        stack = [i]
        tans = arr[i]
        visited[i] = 1
        while stack:
            v = stack.pop()
            tans = min(tans, arr[v])
            for node in m[v]:
                if not visited[node]:
                    visited[node] = 1
                    stack.append(node)
        ans += tans

print(ans)