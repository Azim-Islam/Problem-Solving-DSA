from collections import defaultdict
from collections import deque

def bfs(n:int, s: int):
    visited = [0]*(n+1)
    dist = [0]*(n+1)
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        node = q.popleft()
        for i in adjc[node]:
            if not visited[i]:
                dist[i] = dist[node] + 1
                q.append(i)
                visited[i] = 1
    return dist

for t in range(int(input())):
    n = int(input())
    r = int(input())
    adjc = defaultdict(list)
    for i in range(r):
        u, v = map(int, input().split())
        adjc[u].append(v)
        adjc[v].append(u)
    s, d = map(int, input().split())
    l1 = bfs(n, s)
    l2 = bfs(n, d)
    dist = [l1[i]+l2[i] for i in range(n+1)]
    dist[s] = 0
    print(f"Case {t+1}: {max(dist)}")