for _ in range(int(input())):
    n = int(input())
    arr = [i for i in range(1, n+1)]
    for i in range(n-1, 0, -2):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    print(*arr)
