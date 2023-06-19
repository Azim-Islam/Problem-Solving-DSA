from math import ceil
for _ in range(int(input())):
    n, k, g = map(int, input().split())
    t = k*g
    c = ceil(g/2) - 1
    if c*n >= t:
        print(t)
    else:
        x = t - (n-1)*c
        d = x%g
        if d > c:
            print(t-(x+(g-d)))
        else:
            print(t - (x-d))