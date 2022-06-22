from math import sqrt
for _ in range(int(input())):
    p, q = map(int, input().split())
    r, s = map(int, input().split())
    n, m = map(int, input().split())

    X = sqrt(m**2-n**2)
    print(X + (q/p) * (1-p/q-r/s) * X + (q/p)*(r/s)*X)
    print((q/p) * (1-p/q-r/s) * X)