for _ in range(int(input())):
    n = int(input())
    if n%2:
        print(*[i for i in range((n+1)//2, 0, -1)], *[i for i in range((n+1)//2+1, n+1)])
    else:
        print("-1")