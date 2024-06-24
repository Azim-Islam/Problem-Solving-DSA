n = int(input())
ajcn = {}
for i in range(n):
    u, d, *v = list(map(int, input().split()))
    v.sort()
    ajcn[u] = v

stack = []
d = [0]*(n+1)
f = [0]*(n+1)
visited = [0]*(n+1)

ptr = 0

for i in range(1, n+1):
    if not visited[i]:
        stack.append(i)
        ptr += 1
        visited[i] = 1
        d[i] = ptr
    while stack:
        for i in ajcn[stack[-1]]:
            if not visited[i]:
                # print(f"{i} not visited for parent {stack[-1]}")
                stack.append(i)
                visited[i] = 1
                ptr += 1
                d[i] = ptr
                break
        else:
            ptr += 1
            f[stack.pop()] = ptr

for i in range(1, n+1):
    print(i, d[i], f[i])