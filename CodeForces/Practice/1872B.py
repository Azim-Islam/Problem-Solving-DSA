for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    t = float('inf')
    for d, s in arr:
        v = s//2 + 1
        v = s - (s//2 + 1)
        t = min(t, d+v)
    print(t)