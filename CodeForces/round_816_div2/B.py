for _ in range(int(input())):
    n, k, b, s = map(int, input().split())
    c_s = s
    if s < b*k:
        print("-1")
    else:
        f1 = min(int(k*(b+0.99999999)), s)
        arr = [f1]
        s = s-f1
        for i in range(n-1):
            nv = min([k-1, s])
            arr.append(nv)
            s -= nv
        if s > 0:
            print("-1")
        else:
            print(*arr)