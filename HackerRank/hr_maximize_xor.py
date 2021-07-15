from math import log, ceil
l = int(input())
r = int(input())

if log(l^r, 2) == 1:
    print(int("1"*2, 2))
else:
    ans = int("1"*ceil(log(l^r, 2)), 2)