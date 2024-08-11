for _ in range(int(input())):
    n = int(input())
    arr =  list(map(int, input().split()))
    ans = 0
    for i in range(0, n-1, 2):
        ans += arr[i]|arr[i+1]

    print(ans)