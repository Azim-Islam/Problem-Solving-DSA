from math import factorial
import sys

for line in sys.stdin:
    n = int(line.strip())
    if n >= 0:
        if n > 13:
            print("Overflow!")
        elif n < 8:
            print("Underflow!")
        else:
            ans = factorial(n)
            print(ans)
    elif n < 0:
        if n%2 == 0:
            print("Underflow!")
        else:
            print("Overflow!")