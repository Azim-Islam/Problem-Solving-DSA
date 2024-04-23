def check(mid, k):
    print("?", 1, mid)
    q = (mid) - int(input())
    if q >= k:
        return 1
    else:
        return 0

n, t = map(int, input().split())
k = int(input())

lo = 1
hi = n
while lo < hi:
    mid = (lo+hi)//2
    if check(mid, k):
        hi = mid
    else:
        lo = mid+1

print("!", hi)