from math import factorial
import sys

for line in sys.stdin:
    n = int(line.strip())
    ans = factorial(n)
    while ans%10 == 0:
        ans = ans//10
    string = "{} -> {}".format(n, ans%10)
    padding = " "*(10 - len(string))
    print(padding+string)
