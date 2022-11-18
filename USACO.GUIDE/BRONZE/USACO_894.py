from collections import defaultdict
input = open('planting.in', 'r').readline
print = lambda x : open('planting.out', 'w').write(str(x)+'\n')

def solve():
    n = int(input())
    d = defaultdict(list)
    for i in range(n-1):
        u, v = input().split()
        d[u].append(v)
        d[v].append(u)

    colors = 0
    # print(d)
    for k in d:
        colors = max(colors, len(d[k])+1)

    print(colors)

solve()