from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cats = [0]+list(map(int, input().split()))

adj = defaultdict(list)
c = [0]*(n+1)
visited = [0]*(n+1)
deg = [0]*(n+1)
ans = 0
stack = []

for i in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    deg[u] += 1
    deg[v] += 1

stack.append(1)
deg[1] += 1
# c[1] += cats[1]
visited[1] = 1
cons = cats[1]
cs = [0]*(n+1)
cs[1] = cons

while stack:
    for i in adj[stack[-1]]:
        if not visited[i]:
            if cats[i] and cons+1 <= m:
                cons += 1
                stack.append(i)
                visited[i] = 1
                break
            elif not cats[i]:
                cons = 0
                visited[i] = 1
                stack.append(i)
                break
            else:
                stack[1]
    else:
        v = stack.pop()
        if deg[v] == 1:
            ans += 1
print(ans)