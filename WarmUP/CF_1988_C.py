from collections import Counter
from math import log, ceil
for t in range(int(input())):
    n = int(input())
    first = n
    ans = [n]
    for _ in range(Counter(bin(n))['1']):
        x = ans[-1]
        for i in range(ceil(log(n, 2))):
            m = 1 << i
            if n&m:
                x ^= m
                if x|ans[-1] == n and x < ans[-1]: ans.append(x); break
    print(len(ans))
    print(*ans[::-1])