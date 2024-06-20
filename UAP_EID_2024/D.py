""""
1
4 2
4 3 5 3
"""


import sys

input = sys.stdin.readline

def check(arr, s, r, m):
    n = len(arr)
    c = 0
    for v in arr:
        if v < r:
            c += (r-v)
    
    if s - (n*r - c) >= m:
        return 1
    return 0


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    s = sum(arr)
    lo = 0
    hi = 10**18+1000
    ans = -1
    # print(f"test {m}")
    while lo < hi:
        mid = lo + (hi-lo+1)//2
        if check(arr, s, mid, m):
            lo = mid
            ans = lo
        else:
            hi = mid -1
        

    if ans == -1 and check(arr, s, 0, m):
        print(0)
    else:
        print(ans)
        