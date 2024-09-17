from math import sqrt
for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print("YES")
    else:
        if sqrt(n/4) == int(sqrt(n/4)) or sqrt(n/2) == int(sqrt(n/2)):
            print('YES')
        else:
            print("NO")
    # print("NO")