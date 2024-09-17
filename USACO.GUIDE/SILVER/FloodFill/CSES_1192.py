import gc
gc.disable()
import sys
input = sys.stdin.readline
out = sys.stdout

def solve():
    n, m = map(int, input().split())

    MM = []
    vis = [[0]*(m+1) for _ in range(n+1)]
    c = 0

    for _ in range(n):
        MM.append(list(input()))

    for i in range(n):
        for j in range(m):
            if MM[i][j] == "." and not vis[i][j]:
                c += 1
                stack = [[i, j]]
                vis[i][j] = 1
                while stack:
                    a, b  = stack.pop()
                    up_x = min(a + 1, n-1)
                    do_x = max(0, a - 1)

                    up_y = min(b + 1, m-1)
                    do_y = max(b - 1, 0)

                    if MM[up_x][b] == "." and not vis[up_x][b]:
                        stack.append([up_x, b])
                        vis[up_x][b] = 1
                    if MM[do_x][b] == "." and not vis[do_x][b]:
                        stack.append([do_x, b])
                        vis[do_x][b] = 1
                    if MM[a][do_y] == "." and not vis[a][do_y]:
                        stack.append([a, do_y])
                        vis[a][do_y] = 1
                    if MM[a][up_y] == "." and not vis[a][up_y]:
                        stack.append([a, up_y])
                        vis[a][up_y] = 1
    print(c, file=out)


solve()