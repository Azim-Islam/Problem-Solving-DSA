from sys import stdin
import os


n, k = map(int, stdin.readline().split())
count = 0
M = 12*pow(10, 7)
i = list(map(int, os.read(0, M).split()))

for _ in i:
    if not _ % k:
        count += 1

print(count)
