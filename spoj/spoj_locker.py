m = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    print(int(pow(3, n/3))%m)