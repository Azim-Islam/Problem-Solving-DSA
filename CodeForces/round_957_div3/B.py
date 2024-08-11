for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = 0
    for i in arr[1:]:
        ans += (i-1) + i
    print(ans)