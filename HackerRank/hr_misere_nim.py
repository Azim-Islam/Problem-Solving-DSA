

from functools import reduce
from operator import xor
from collections import Counter 


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = reduce(xor, arr)
    counted = Counter(arr)
    if ans == 0:
        if (len(list(counted.keys())) == 1 and list(counted.keys())[0] == 1 and counted[1]%2 == 0):
            print("First")
        else:
            print("Second")
    if ans > 0:
        if (len(list(counted.keys())) == 1 and list(counted.keys())[0] == 1 and counted[1]%2 == 1):
            print("Second")
        else:
            print("First")