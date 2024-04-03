def check(arr, t, time):
    count = 0
    for i in arr:
        count += time//i
    if count >= t:
        return True
    else:
        return False


n, t = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lo = 1
hi = 2*10**18

while lo < hi:
    mid = (lo + hi)//2
    if check(arr, t, mid):
        hi = mid
    else:
        lo = mid + 1
    
print(hi)
