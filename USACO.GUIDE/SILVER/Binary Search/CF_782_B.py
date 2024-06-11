n = int(input())
arr_p = list(map(int, input().split()))
arr_v = list(map(int, input().split()))


def check(arr_p, arr_v, time):
    left, right = float('-inf'), float('inf')
    for i in range(0, n):
        l, r = max(1, arr_p[i] - arr_v[i]*time), arr_p[i] + arr_v[i]*time
        left = max(left, l)
        right = min(right, r)
    if right >= left:
        return 1
    return 0

lo = 0
hi = 10**9

for _ in range(100):
    mid = (hi+lo)/2
    # print(mid, hi, lo)
    if check(arr_p, arr_v, mid):
        # print("True for", mid)
        hi = mid
    else:
        lo = mid
    # i += 1


        
        
# print(check(arr_p, arr_v, 1.400000000001))
print(hi)