import sys

from bisect import bisect_right as br
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n, k, q = map(int, input().split())
    arr_point =[0] + list(map(int, input().split()))
    arr_time =[0] + list(map(int, input().split()))
    d = defaultdict(int)
    out = []
    for p, t in zip(arr_point, arr_time):
        d[p] = t

    for __ in range(q):
        r = int(input())
        if r == n:
            out.append(str(arr_time[-1]))
        else:
            idx = br(arr_point, r) - 1
            p1, p2 = arr_point[idx], arr_point[idx+1]
            t1, t2 = d[p1], d[p2]
            # v0 = abs(p1-p2)/abs(t1-t2)
            # s = 
            ans = d[p1] + int((abs(p1-r) * abs(t1-t2))//abs(p1-p2))
            out.append(str(ans))

    print(" ".join(out))