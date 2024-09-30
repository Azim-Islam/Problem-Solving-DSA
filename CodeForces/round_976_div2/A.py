import gc
gc.disable()
import sys
from math import ceil, log

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    if k > n:
        print(n)
    else:
        if k == 1:
            print(n)
        else:
            c = 0
            while n != 0: 
                v = (n//k**int(log(n, k)))
                c += v
                n = n - k**(log(n,k)//1) * v
            print(int(c))