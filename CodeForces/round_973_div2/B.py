import gc
gc.disable()
from math import ceil
import sys

input = sys.stdin.readline
def solve():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        for i in range(n-2):
            arr[-2] = arr[-2] - arr[i]
        
        print(arr[-1]-arr[-2])


solve()