from collections import deque
from heapq import *

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = arr
    min_h = [i for i in range(n, 0, - 1)]
    max_h = [i for i in range(1, n+1)]
    # for i in range(1, n+1):
    #     heappush(min_h, i)
    # for i in range(1, n+1):
    #     heappush(max_h, -i)

    i = 0
    j = n-1
    f = True

    while i < j:
        # mn = heappop(min_h) ; heappush(min_h, mn)
        # mx = -heappop(max_h) ; heappush(max_h, -mx)
        mn = min_h[-1]
        mx = max_h[-1]

        if d[i] == mn:
            # heappop(min_h)
            min_h.pop()
            i += 1
        elif d[i] == mx:
            # heappop(max_h)
            max_h.pop()
            i += 1
        elif d[j] == mn:
            # heappop(min_h)
            min_h.pop()
            j -= 1
        elif d[j] == mx:
            # heappop(max_h)
            max_h.pop()
            j -= 1
        else:
            print(i+1, j+1)
            f = False
            break
    if f:
        print("-1")