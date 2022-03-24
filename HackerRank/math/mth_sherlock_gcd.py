from functools import reduce
from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if reduce(gcd, arr) > 1:
        print("NO")
    else:
        print("YES")