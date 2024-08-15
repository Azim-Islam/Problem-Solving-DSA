for _ in range(int(input())):
    n = int(input())
    arr = [-1] + list(map(int, input().split()))

    ans = 3

    for i in range(1, n+1):
        if i == arr[arr[i]]:
            print(2)
            break
    else:
        print(3)