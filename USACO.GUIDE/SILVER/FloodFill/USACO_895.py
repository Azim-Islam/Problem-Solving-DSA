import gc
gc.disable()

def solve():
    input = open("perimeter.in", 'r').readline
    out = open("perimeter.out", 'w')

    def calc_peri(MM, i, j, n):
        n = len(MM)
        ret = 0
        ux = min(i + 1, n-1)
        dx = max(i - 1, 0)
        uy = min(j + 1, n-1)
        dy = max(j - 1, 0)
        if MM[ux][j] != "#":
            ret += 1
        if MM[dx][j] != "#":
            ret += 1
        if MM[i][uy] != "#":
            ret += 1
        if MM[i][dy] != "#":
            ret += 1
        return ret
        

    n = int(input())

    MM = [list("."*(n+2))]
    for i in range(n):
        MM.append(["."]+list(input()) + ["."])
    MM.append(list("."*(n+2)))
    # print(len(MM), len(MM[0]))
    n += 2
    vis = [[0]*(n) for _ in range(n)]
    comp = []
    for i in range(n):
        for j in range(n):
            if not vis[i][j] and MM[i][j] == "#":
                stack = [[i, j]]
                vis[i][j] = 1
                area = 1
                peri = 0
                while stack:
                    a, b = stack.pop()
                    peri += calc_peri(MM, a, b, n)
                    ux = min(a + 1, n-1)
                    dx = max(a - 1, 0)
                    uy = min(b + 1, n-1)
                    dy = max(b - 1, 0)
                    if MM[ux][b] == "#" and not vis[ux][b]:
                        area += 1
                        stack.append([ux, b])
                        vis[ux][b] = 1
                    if MM[dx][b] == "#" and not vis[dx][b]:
                        area += 1
                        stack.append([dx, b])
                        vis[dx][b] = 1
                    if MM[a][uy] == "#" and not vis[a][uy]:
                        area += 1
                        stack.append([a, uy])
                        vis[a][uy] = 1
                    if MM[a][dy] == "#" and not vis[a][dy]:
                        area += 1
                        stack.append([a, dy])
                        vis[a][dy] = 1

                comp.append([area, peri])

    aa, pp = 0, 0
    for a, p in comp:
        if a > aa:
            aa = a
            pp = p

    for a, p in comp:
        if aa == a and pp > p:
            pp = p

    print(aa, pp, file=out)

solve()