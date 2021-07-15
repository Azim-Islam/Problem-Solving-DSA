from math import gcd
for _ in range(int(input())):
    a,b = map(int, input().split())
    gcd_ = gcd(a, b)
    print((a*b)//(gcd_*gcd_))