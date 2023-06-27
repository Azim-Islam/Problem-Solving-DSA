from bisect import bisect
from collections import defaultdict

n, m = map(int, input().split())

arr_c = list(map(int, input().split()))
arr_t = list(map(int, input().split()))

ans = 0
for c in arr_c:
    idx = bisect(arr_t, c) - 1
    ans = max(ans, min([abs(arr_t[idx]-c),  abs(arr_t[min(idx+1, m-1)]-c), abs(arr_t[max(idx-1, 0)]-c)]))


print(ans)