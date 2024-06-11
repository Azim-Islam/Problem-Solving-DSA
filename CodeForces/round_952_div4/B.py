for _ in range(int(input())):
    n = int(input())
    ans = 0
    v = 0
    for i in range(2, n+1):
        s = 0
        for j in range(1, n//i+1):
            s += i*j
        if s >= ans:
            ans = s
            v = i

    print(v)