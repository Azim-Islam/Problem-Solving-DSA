import gc
gc.disable()

from collections import Counter, defaultdict
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    queries = list(map(int, input().split()))
    prev = n-1
    d = defaultdict(int)
    d[prev] = 1
    for i in range(2, n+1):
        ans = n-i + (prev - (i-2))
        d[ans] += 1
        # print(i, ans)
        vv = ans - (n-i)
        d[vv] += arr[i]-arr[i-1] - 1
        prev = ans
        # ans1 = 
        

    # print(d)
    output = []
    for qq in queries:
        output.append(str(d[qq]))
    print(" ".join(output))