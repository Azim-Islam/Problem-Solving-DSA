from math import log
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(int(log(r, 2)))

    