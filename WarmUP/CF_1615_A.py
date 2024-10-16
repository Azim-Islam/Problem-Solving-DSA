import gc
# gc.disable()

from math import ceil, floor, log


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(ceil(log(max(arr), 2))*(n//2+1)):
        arr.sort()
        v = (arr[-1]-arr[0])//2
        arr[0] += v
        arr[-1] -= v

    arr.sort()
    assert arr[-1] - arr[0] >= 0
    print(arr[-1]-arr[0])