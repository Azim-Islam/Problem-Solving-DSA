from collections import defaultdict
import gc
gc.disable()

input = open("wormsort.in", "r").readline
# out = open("wormsort.out", "w")

def check(adj, arr, min_width):
    visited = [0]*(len(arr)+1)
    for i in range(1, len(arr)+1):
        if not visited[i]:
            stack = [i]
            visited[i] = i
            while stack:
                v = stack.pop()
                for n in adj[v]:
                    if not visited[n[0]] and n[1] >= min_width:
                        visited[n[0]] = i
                        stack.append(n[0])

    for i, v in enumerate(arr):  
        if not(visited[i+1] == visited[v]):
            return False
    return True



N, M = map(int, input().split())
arr = list(map(int, input().split()))
adj = defaultdict(list)


for i in range(M):
    a, b, w = map(int, input().split())
    adj[a].append([b, w])
    adj[b].append([a, w])

hi = 10**9+1
lo = 1

while lo < hi:
    mid = (hi + lo + 1)//2
    if check(adj, arr, mid):
        lo = mid
    else:
        hi = mid - 1
# print(check(adj, arr, 9))

print(lo if lo != 10**9+1 else -1, file=open("wormsort.out", "w"))
# print(lo if lo != 10**9+1 else -1)



