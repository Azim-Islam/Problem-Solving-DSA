from collections import defaultdict
from math import sqrt
import sys

#AC
input = sys.stdin.readline
        
def check(c, i, m): #O(sqrt(n))
    for j in range(1, int(sqrt(i))+1):
        if i%j == 0 and j <= m:
            c[i].add(j)
            if i//j <= m:
                c[i].add(i//j)

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    c = defaultdict(set) # This dictionary contains divisors (up to 'm') of [Ai] number. #Complexity sqrt(n)
    for i in arr:
        check(c, i, m)
    d = defaultdict(int)
    j = 0
    ans = float('inf')

    # Here, if there no valid solution, we extend right pointer (j) until a valid solution.
    # While a valid solution is found we move the left pointer (i) to right while keeping the left right pointer (j) stationary and repeat.
    for i in range(n): #O(n)
        while j < n:
            if len(d) == m:
                ans = min(ans, abs(arr[i]-arr[j-1]))
                break
            else:
                for k in c[arr[j]]:
                    d[k] += 1
                j += 1
        if len(d) == m:
                ans = min(ans, abs(arr[i]-arr[j-1]))
        
        for k in c[arr[i]]:
            d[k] -= 1
            if d[k] == 0:
                del d[k]

    if ans == float('inf'):
        print("-1")
    else:
        print(ans)