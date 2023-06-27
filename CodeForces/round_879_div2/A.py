from math import ceil
from functools import reduce
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mul = reduce(lambda x, y: x*y, arr)
    sm = reduce(lambda x, y: x+y, arr)
    ans = 0
    if mul < 0:
        ans += 1
    if sm < 0:
        a = ceil(abs(min(0, ans*2+sm))/2)
        ans += a + a%2
    print(ans)