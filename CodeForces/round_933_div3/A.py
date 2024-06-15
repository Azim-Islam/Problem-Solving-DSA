for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    c_arr = list(map(int, input().split()))
    ans = 0
    for i in b_arr:
        for j in c_arr:
            if i+j <= k:
                ans += 1

    print(ans)
