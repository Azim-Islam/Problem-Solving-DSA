from collections import defaultdict

def no_conn(v1, v2, v3):
    s1 = list(v3.difference(v1))
    s2 = list(v1.difference(v2))
    s3  = list(v2.difference(v1))
    if s1:
        return (1, s1[0])
    if s2:
        return (s2[0], 1)
    if s3:
        return (1, s3[0])

def DFS(G):
    stack = [1]
    visited = set()

    visited.add(1)

    while stack:
        v = stack.pop()
        for node in G[v]:
            if node not in visited:
                visited.add(node)
                stack.append(node)
            
    return visited
    

n, m = map(int, input().split())
G = defaultdict(list)
G_prime = defaultdict(list)


for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G_prime[b].append(a)



v1 = DFS(G)
v2 = DFS(G_prime)
v3 = set([i+1 for i in range(n)])

if len(v1) == n and len(v2) == n:
    print("YES")
else:
    print("NO")
    print(*no_conn(v1, v2, v3))