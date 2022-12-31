import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            count = True
        if arr[i] < arr[i+1] and count:
            print("NO")
            break
    else:
        print("YES")