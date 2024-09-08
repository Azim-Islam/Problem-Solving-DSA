from collections import defaultdict
from bisect import bisect_right as bl
import sys
input = sys.stdin.readline

def return_min(a, b):
    ans = float('inf')
    for v in a:
        idx = bl(b, v)
        ans = min(ans, (v-b[max(idx-1, 0)])**2)
        ans = min(ans, (v-b[min(idx, len(b)-1)])**2)
        ans = min(ans, (v-b[min(idx+1, len(b)-1)])**2)
    return ans


for _ in range(int(input())):
    n, m = map(int, input().split())
    d = defaultdict(list)

    for i in range(m):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    visited = defaultdict(int)
    components = []
    for i in range(1, n+1):
        if not visited[i]:
            components.append([i])
            stack = [i]
            visited[i] = 1
            while stack:
                v = stack.pop()
                for nn in d[v]:
                    if not visited[nn]:
                        stack.append(nn)
                        components[-1].append(nn)
                        visited[nn] = 1
    
    for arr in components:
        arr.sort()
        # print(arr)

        
    # print(components)

    F = True
    for arr in components:
        if arr[0] == 1 and arr[-1] == n:
            F = False
            break

    if len(components) == 1 or F == False:
        print("0")

    elif len(components) == 2:
        a = components[0]
        b = components[1]
        print(return_min(a, b))
    else:
        a = components[0]
        # c = components[1] if components[1][-1] == n else components[2]
        # b = components[1] if components[1][-1] != n else components[2] 
        bidx = -1 
        for i, arr in enumerate(components):
            if arr[-1] == n:
                bidx = i
                break
        b = components[bidx]
        ans = return_min(a, b)
        mid_component = []
        for i, arr in enumerate(components):
            ans = min(ans, return_min(arr, a) + return_min(arr, b))




        print(ans)