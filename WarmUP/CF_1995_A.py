for _ in range(int(input())):
    n, k = map(int, input().split())
    c = 0
    # k += n if n%2 else 0
    if k:
        k -= n
        n -= 1
        c += 1

    while k > 0:
        if n >= k:
            k -= n
            c += 1
            n -= 1
        else:
            k -= n*2
            c += 2
            n -= 1

    print(c)