from math import gcd
for _ in range(int(input())):
    # n = int(input())
    l, r= map(int, input().split())
    ans = 0
    
    while l <= r:
        if l%2 == 0:
            l += 1
        if (r - l + 1) >= 3:
            ans += 1
        l += 3
    
    print(ans)