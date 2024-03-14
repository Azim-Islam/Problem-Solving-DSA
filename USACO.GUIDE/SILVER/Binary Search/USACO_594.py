from bisect import bisect_right as br

input = open('angry.in', 'r').readline
out = open('angry.out', 'w')

def check(arr, R, K):
    start = 0
    for i in range(K):
        idx = br(arr, arr[start]+R*2) - 1
        start = idx + 1
        if start >= len(arr):
            return 1

    if start == len(arr):
        return 1
    else:
        return 0

n, k = map(int, input().split())
arr =[]

for _ in range(n):
    arr.append(int(input()))

arr.sort()

#Binary Search
hi = 2*10**9
lo = 0
while(lo < hi):
    mid = (lo+hi)//2
    if check(arr, mid, k):
        hi = mid
    else:
        lo = mid + 1

print(hi, file=out)