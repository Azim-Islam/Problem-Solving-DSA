from math import gcd
from functools import reduce

f = lambda x,y : gcd(x,y)
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dcg = reduce(f, arr)
    s = sum(arr) 
    print(dcg, s//dcg)