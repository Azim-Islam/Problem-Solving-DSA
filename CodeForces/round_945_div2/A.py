for _ in range(int(input())):
    a, b, c = map(int, input().split())

    arr = [a, b, c]
    ans = 0
    while arr[-1] != 0 and arr[-2] != 0:
        arr[-1] -= 1
        arr[-2] -= 1
        ans += 1
        arr.sort()
    if arr[0]%2 != 0 or arr[1]%2 != 0 or arr[2]%2 != 0:
        print(-1)
    else:
        print(ans)
