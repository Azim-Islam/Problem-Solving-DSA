for _ in range(int(input())):
    n, d, r = map(int, input().split())
    pd, pr = d, r
    i = 1
    while pd != pr:
        pd += d
        pr += r
    print(i)