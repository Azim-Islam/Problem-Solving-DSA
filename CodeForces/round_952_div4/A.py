for _ in range(int(input())):
    a, b = input().split()
    a = list(a)
    b = list(b)
    a[0], b[0] = b[0], a[0]
    print("".join(a), "".join(b))