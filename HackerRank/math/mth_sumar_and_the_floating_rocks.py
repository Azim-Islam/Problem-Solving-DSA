from math import sqrt
from math import gcd

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(abs(gcd(y2-y1, x2-x1) - 1))