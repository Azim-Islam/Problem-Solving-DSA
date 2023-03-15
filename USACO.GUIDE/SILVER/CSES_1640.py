from collections import defaultdict
import sys

input = sys.stdin.readline

def solve(arr, d):
    i1 = -1
    i2 = -1
    for i, v in enumerate(arr):
        if str(x-v) in d:
            # if x-v != v:
            #     i1 = i
            #     i2 = d[x-v]
            #     return (i1, i2)
            # else:
            for i0 in d[str(x-v)]:
                if i0 != i:
                    i1 = i
                    i2 = i0
                    return (i1, i2)
    return (i1, i2)

n, x = map(int, input().split())
arr = list(map(int, input().split()))


d = defaultdict(list)

for i,v  in enumerate(arr):
    d[str(v)].append(i)


                    
i1, i2 = solve(arr, d)
i1 += 1
i2 += 1
if i1 and i2:
    print(min(i1, i2), max(i1, i2))
else:
    print("IMPOSSIBLE")