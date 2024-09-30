import gc

gc.disable()
import sys
from math import ceil, sqrt
import decimal

decimal.getcontext().prec = 40

input = sys.stdin.readline



for _ in range(int(input())):
    k = int(input())
    t = decimal.Decimal(k).sqrt().__round__()
    print(k+t)