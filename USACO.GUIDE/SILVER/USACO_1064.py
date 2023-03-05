from collections import defaultdict

c0 = 0
x0 = 2
y0 = 3
d0 = 1


n = int(input())
arr = []
for i in range(n):
    inp = input().split()
    d, x, y = inp[0], int(inp[1]), int(inp[2])
    arr.append([i+1, d, x, y])

comp = sorted(arr, key=lambda x: (x[2], x[3]))
# d = defaultdict()
for i in range(n):
    comp[i][2] = i

comp = sorted(arr, key=lambda x: x[3])

for i in range(n):
    comp[i][3] = i

m = [[0]*(n+1) for _ in range(n+1)]

for c in comp:
    m[c[2]][c[3]] = [c[0], 0] #cow id, direction, distance

print("\n".join(map(str, m)))

d = defaultdict(set)

for i in range(n*n+1):
    for c in comp:
        if c[d0] == 'N':
            curr_x = c[x0]
            curr_y = c[y0]
            curr_dist = m[curr_x][curr_y][-1]
            if curr_y+1 <= n:
                if m[curr_x][curr_y+1] and curr_dist + 1 != m[curr_x][curr_y+1][-1]:
                    d[m[curr_x][curr_y+1][c0]].add(c[c0]) #cow in m blocks the current cow
                else:
                    m[curr_x][curr_y+1] = [c[c0], curr_dist+1]
                    c[y0] = min(n, c[y0]+1)
        else:
            curr_x = c[x0]
            curr_y = c[y0]
            curr_dist = m[curr_x][curr_y][-1]
            if curr_x+1 <= n:
                if m[curr_x+1][curr_y] and curr_dist + 1 != m[curr_x+1][curr_y][-1]:
                    d[m[curr_x+1][curr_y][c0]].add(c[c0]) #cow in m blocks the current cow
                else:
                    m[curr_x+1][curr_y] = [c[c0], curr_dist+1]
                    c[x0] = min(n, c[x0]+1)

for i in range()