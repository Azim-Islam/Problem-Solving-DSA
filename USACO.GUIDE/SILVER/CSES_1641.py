from collections import defaultdict
import sys
input = sys.stdin.readline 
from bisect import bisect

n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr = [[v, i] for i, v in enumerate(arr)]
arr.sort()
arr_v = [arr[i][0] for i in range(n)]

def solve(arr, arr_v, n, x):
    d = defaultdict(list)
    for i in range(n):
        d[arr_v[i]].append(i)
    for i in range(n):
        for j in range(i+1, n):
            v = arr[i][0]+arr[j][0]
            if x-v in d:
                for k in d[x-v]:
                    if i < k < j:
                        print(arr[i][1]+1, arr[j][1]+1, arr[k][1]+1)
                        return
    print("IMPOSSIBLE")

solve(arr, arr_v, n, x)