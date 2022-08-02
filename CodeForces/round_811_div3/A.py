for _ in range(int(input())):
    n, H, M = map(int, input().split())
    ans = []
    for i in range(n):
        h, m = map(int, input().split())
        if h > H:
            a = h - H
            if m >= M:
                b = m - M
            if m < M:
                a -= 1
                b = m - M + 60
            ans.append((a, b))
        if h < H:
            a = h - H + 24
            if m >= M:
                b = m - M
            if m < M:
                a -= 1
                b = m - M + 60
            ans.append((a, b))
        if h == H:
            a = 0
            if m >= M:
                b = m - M
            if m < M:
                a = 23
                b = m - M + 60
            ans.append((a, b))

    ans.sort()
    print(ans[0][0], ans[0][1])