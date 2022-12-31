from itertools import accumulate
from collections import defaultdict
import sys

import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

t = int(input())




def solve():
    n = int(input())
    d = defaultdict(int)
    arr = list(map(int, list(input().strip())))
    cum = list(accumulate(arr, initial=0))
    for i in range(0, len(cum)):
        d[cum[i] - i] += 1
    ans = 0
    for v in d.values():
        ans += v*(v-1)//2
    print(ans)

for i in range(t):
    solve()