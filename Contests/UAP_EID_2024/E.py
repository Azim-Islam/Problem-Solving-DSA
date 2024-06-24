mod = 10**9+7
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(pow(m, n, mod))