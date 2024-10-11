import gc
gc.disable()
import random
import sys
from math import ceil, floor, sqrt

input = sys.stdin.readline


def s1(n, arr):
    for i in range(n*n+1):
        arr.sort()
        v = (arr[-1]-arr[0])//2
        arr[0] += v  
        arr[-1] -= v
        # print(arr)

    arr.sort()
    return arr[-1]-arr[0]

def s2(n, arr):
    for i in range(n*n+1):
        arr.sort()
        while arr[0] < arr[-1]:
            arr[0] += 1
            arr[-1] -= 1

    arr.sort()
    return arr[-1]-arr[0]


for t in range(0, 100):
    n = random.randint(2, 101)
    arr = [random.randint(1, 1000) for i in range(n)]
    print(s1(n, arr[:]) == s2(n, arr[:]))
