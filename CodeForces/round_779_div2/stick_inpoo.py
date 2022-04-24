from math import sqrt


for _ in range(int(input())):
    P, Q = map(int, input().split())
    R, S = map(int, input().split())
    N, M = map(int, input().split())

    total_length = sqrt(M**2 - N**2)*(Q/P)
    ans = total_length - total_length*(R/S) - sqrt(M**2 - N**2)

    print(total_length, ans)