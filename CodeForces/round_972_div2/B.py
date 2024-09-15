from dataclasses import field
import sys
input = sys.stdin.readline
out = sys.stdout
from bisect import bisect_left as bl
ans = []
for _ in range(int(input())):
    # n = int(input())
    n, m, q = map(int, input().split())
    bb = sorted(list(map(int, input().split())))
    # print(q)
    pp = list(map(int, input().split()))
    for p in pp:
        b = bb[-1]
        a = bb[0]
        if p > b:
            ans.append(n-b)
        elif p < a:
            ans.append(a-1)
        else:
            idx = bl(bb, p)
            b = bb[idx]
            a = bb[idx-1]
            ans.append((b-a)//2)

    
print("\n".join(map(str, ans)), file=out)
