import gc
from re import split
gc.disable()

from collections import Counter
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    s1 = 0
    s2 = 0

    c = 0
    m = float('-inf')
    for i in range(0, n, 2):
        if arr[i] > m:
            m = arr[i]
        c += 1

    s1 = c + m

    c = 0
    m = float('-inf')
    for i in range(1, n, 2):
        if arr[i] > m:
            m = arr[i]
        c += 1
    s2 = c + m
    print(max(s1, s2))