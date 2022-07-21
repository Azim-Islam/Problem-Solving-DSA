for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ch = [-1]*(n+1)
    ans = [0]*(n+1)
    for i in range(n):
        if ch[arr[i]] == -1:
            ans[arr[i]] += 1
        elif ch[arr[i]] >= 0:
            dist = abs(ch[arr[i]] - i - 1)
            if dist%2 == 0:
                # print(arr[i], ch[arr[i]], i)
                ans[arr[i]] += 1
        ch[arr[i]] = i

    print(" ".join([str(ans[i]) for i in range(1, n+1)]))
