for _ in range(int(input())):
    n, k = map(int, input().split())
    if k < n//2:
        print(k*2+1)
    else:
        print((n-k-1)*2)