for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = float('inf')
    for i in arr:
        t = i
        while t%k != 0:
            t += 1
        ans = min(ans, t-i)
    
    if k == 4:
        c = 0
        for i in arr:
            if i%2 == 0:
                c += 1
        if c >= 2:
            ans = 0
        else:
            ans = min(ans, 2 - c)

    print(ans)