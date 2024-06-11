input = open('closing.in', 'r').readline
fout = open('closing.out', 'w')


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
closed = [0]*(n+1)

def FC(adj, closed, n):
    visited = [0]*(n+1)
    stack = []
    node = 1
    for i in range(1, n+1):
        if not closed[i]:
            node = i
            break
    # DFS
    stack.append(node)
    visited[node] = 1
    while stack:
        v = stack.pop()
        for child in adj[v]:
            if not visited[child] and not closed[child]:
                stack.append(child)
                visited[child] = 1

    for i in range(1, n+1):
        if visited[i] == 0 and closed[i] == 0:
            return 0
    return 1


for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

pops = []
for i in range(n):
    pops.append(int(input()))




for v in pops:
    if FC(adj, closed, n):
        print("YES", file=fout)
    else:
        print("NO", file=fout)
    closed[v] = 1
