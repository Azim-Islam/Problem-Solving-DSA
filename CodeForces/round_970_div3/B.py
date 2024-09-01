from math import sqrt

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, list(input())))
    count1 = sum(s)
    r = int(sqrt(n))
    if sqrt(n) == int(sqrt(n)):
        if r*2 + (r-2)*2 == count1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

