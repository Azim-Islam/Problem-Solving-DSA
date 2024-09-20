import gc
gc.disable()
from math import ceil
import sys

input = sys.stdin.readline
def solve():
    for _ in range(int(input())):
        n = int(input())
        x, y = map(int, input().split())
        print(max( (n+x-1)//x, (n+y-1)//y))

solve()