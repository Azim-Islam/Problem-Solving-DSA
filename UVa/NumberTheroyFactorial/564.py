from math import factorial
import sys

for line in sys.stdin:
    n = int(line.strip())
    ans = factorial(n)
    print("{}!\n{}".format(n, ans))