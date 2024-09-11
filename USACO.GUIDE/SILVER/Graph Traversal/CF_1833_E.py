from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    components = []
    visited = [0]*(n+1)
    adj = defaultdict(set)
    #DFS
    for i in range(1, n+1):
        if not visited[i]:
            stack = [i]
            visited[i] = 1
            while stack:
                v = stack.pop()
                adj[v].add(arr[v])
                adj[arr[v]].add(v)
                if not visited[arr[v]]:
                    stack.append(arr[v])
                    visited[arr[v]] = 1

    visited = [0]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            stack = [i]
            visited[i] = 1
            components.append([i])
            while stack:
                v = stack.pop()
                for nn in adj[v]:
                    if not visited[nn]:
                        stack.append(nn)
                        visited[nn] = 1
                        components[-1].append(nn)

    ans_min = 0
    ans_max = 0

    extras = 0
    for cmp in components:
        if cmp:
            ans_max += 1
            tt = 0
            for v in cmp:
                if len(adj[v]) != 2:
                    tt += 1
            if extras and tt:
                ans_min += 1
                extras -= 1
                tt -= 1
                extras += tt
            else:
                extras += tt
                
    print(ans_max - ans_min, ans_max)
    # print(components)
