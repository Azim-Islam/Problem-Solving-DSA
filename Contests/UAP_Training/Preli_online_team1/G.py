h, w = map(int, input().split())
marked = [[False for __ in range(w)] for _ in range(h)]
dist = [[0]*w for _ in range(h)]

arr = []



def dfs(i, j, v):
    dist[i][j] = v
    marked[i][j] = True

    if not marked[min(i+1, h-1)][j] and arr[min(i+1, h-1)][j] != "#":
        marked[min(i+1, h-1)][j] = True
        dfs(min(i+1, h-1), j, v+1)
    elif arr[min(i+1, h-1)][j] != "#":
        if dist[min(i+1, h-1)][j] > v+1:
            dfs(min(i+1, h-1), j, v+1)

    if not marked[i][min(j+1, w-1)] and arr[i][min(j+1, w-1)] != "#":
        marked[i][min(j+1, w-1)] = True
        dfs(i, min(j+1, w-1), v+1)
    elif arr[i][min(j+1, w-1)] != "#":
        if dist[i][min(j+1, w-1)] > v+1:
            dfs(i, min(j+1, w-1), v+1)

    if not marked[max(i-1, 0)][j] and arr[max(i-1, 0)][j] != "#":
        marked[max(i-1, 0)][j] = True
        dfs(max(i-1, 0), j, v+1)
    elif arr[max(i-1, 0)][j] != "#":
        if dist[max(i-1, 0)][j] > v+1:
            dfs(max(i-1, 0), j, v+1)

    if not marked[i][max(j-1, 0)] and arr[i][max(j-1, 0)] != "#":
        marked[i][max(j-1, 0)] = True
        dfs(i, max(j-1, 0), v+1)
    elif arr[i][max(j-1, 0)] != "#":
        if dist[i][max(j-1, 0)] > v+1:
            dfs(i, max(j-1, 0), v+1)



for i in range(h):
    arr.append(list(input()))

m = 0
for i in range(h):
    for j in range(w):
        marked = [[False for __ in range(w)] for _ in range(h)]
        dist = [[0]*w for _ in range(h)]
        if arr[i][j] != "#":
            dfs(i, j, 0)
            for i in range(h):
                for j in range(w):
                    # m = max(dist[i][j], m)
                    if m < dist[i][j]:
                        m = dist[i][j]


print(m)

