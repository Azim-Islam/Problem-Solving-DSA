from math import log2
n = int(input())
k = 0
for i in range(62):
    if 2**i > n:
        print(i-1)
        break