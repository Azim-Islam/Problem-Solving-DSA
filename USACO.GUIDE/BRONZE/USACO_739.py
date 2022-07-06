import gc
from collections import defaultdict
read = open('cownomics.in', 'r').readline
# write = lambda x : open('cownomics.out', 'w').write(str(x))


gc.disable()
# read = input
write = print


def solve():
    n, m = map(int, read().split())
    s = []
    p = []
    for i in range(n):
        s.append(list(read()))
    for j in range(n):
        p.append(list(read()))

    a = defaultdict(set)
    for i in range(m):
        for j in range(i+1, m):
            for k in range(j+1, m):
                for o in range(n):
                    a[(i, j, k)].add("".join([p[o][i], p[o][j], p[o][k]]))
    count = 0
    for i in range(m):
        for j in range(i+1, m):
            for k in range(j+1, m):
                for o in range(n):
                    s_ = "".join([s[o][i], s[o][j], s[o][k]])
                    if s_ in a[(i, j, k)]:
                        break
                else:
                    print(i, j, k)
                    count += 1
    write(count)


solve()
