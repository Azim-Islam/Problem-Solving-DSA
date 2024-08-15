for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    A = 0
    B = 0
    i = 0
    for i in range(n):
        if i%2: #bob turn
            v = min(k, arr[i-1]-arr[i])
            k -= v
            B += arr[i]+v
        else:
            A += arr[i]
    print(A-B)