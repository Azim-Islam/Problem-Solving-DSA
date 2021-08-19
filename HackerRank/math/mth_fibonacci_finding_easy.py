n = 10**9 + 7
for _ in range(int(input())):

    U0, U1, n = map(int, input().split())

    for i in range(2, n+1):
        next1 = U0%n + U1%n
        U0 = U1
        U1 = next1
    print(next1)
        
    