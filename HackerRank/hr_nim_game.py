

from functools import reduce
from operator import xor


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = reduce(xor, arr)
    if ans == 0:
        print("Second")
    else:
        print("First")