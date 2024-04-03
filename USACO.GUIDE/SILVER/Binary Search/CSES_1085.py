def check(arr, k, max_sum):
    seg = 1
    s = 0
    for i in arr:
        if s+i <= max_sum:
            s += i
        elif i <= max_sum:
            seg += 1
            s = i
        else:
            return False
        
    if seg <= k:
        return True
    return False
    



n, t = map(int, input().split())
arr = list(map(int, input().split()))


lo = 1
hi = 10**9*2*10**5

while lo < hi:
    mid = (lo + hi)//2
    if check(arr, t, mid):
        hi = mid
    else:
        lo = mid + 1

print(hi)

