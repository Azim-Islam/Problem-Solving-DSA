from math import log, ceil
for _ in range(int(input())):
    n = int(input())
    v = int(log(n-1, 2))
    print(*[i for i in range(2**v+1, n)], *[2**v, 0], *[i for i in range(2**v-1, 0, -1)])