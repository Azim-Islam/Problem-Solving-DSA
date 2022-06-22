from math import factorial
from collections import defaultdict

n = int(input())
while n != 0:
    ans = factorial(n)
    ans_dict = defaultdict(int)
    p = ans
    while p > 0:
        ans_dict[p%10] += 1
        p = p//10
    print("{}! --".format(n))
    print(" ".join(["({}) {}".format(i, ans_dict[i]) for i in range(5)]))
    print(" ".join(["({}) {}".format(i, ans_dict[i]) for i in range(5, 10)]))
    n = int(input())

