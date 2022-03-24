from math import gcd
from functools import reduce

n, q = map(int, input().split())
arr = list(map(int, input().split()))
ans = reduce(gcd, arr)
for _ in range(q):
    offset = int(input())
    if ans != arr[0]:
        print(gcd(ans, offset))
    else:
        print(ans+offset)