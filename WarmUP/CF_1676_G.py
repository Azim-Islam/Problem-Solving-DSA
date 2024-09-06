from collections import Counter


for _ in range(int(input())):
    n = int(input())
    arr = [0, 0] + list(map(int, input().split()))
    s = [0]+list(input())

    leaf_nodes = set([i for i in range(1, n+1)]) - set(arr)

    # print(leaf_nodes)

    whites = [0]*(n+1)
    blacks = [0]*(n+1)
    visited = [0]*(n+1)
    c = Counter(arr)

    for node in leaf_nodes:
        #
        stack = [node]
            
        while stack:
            v = stack.pop()
            if not visited[v]:
                if s[v] == 'W':
                    whites[v] += 1
                elif s[v] == "B":
                    blacks[v] += 1
            visited[v] += 1
            if visited[v] >= c[v]:
                # print(f"from {v} to {arr[v]} - whites {whites[v]} blacks {blacks[v]} - already |{whites[arr[v]]} | {blacks[arr[v]]}")
                whites[arr[v]] = whites[v] + whites[arr[v]]
                blacks[arr[v]] = blacks[v] + blacks[arr[v]]
                stack.append(arr[v])
                
    ans = 0
    # for i in range(1, n+1):
    #     if s[i] == 'W':
    #         whites[i] += 1
    #     else:
    #         blacks[i] += 1

    # for i, v in enumerate(arr):
    #     if v == 1:
    #         whites[1] += whites[i]
    #         blacks[1] += blacks[i]


    for i in range(1, n+1):
        if whites[i] == blacks[i] and whites[i]:
            ans += 1
    # print(s)
    # print(arr)
    # print(whites)
    # print(blacks)
    print(ans)