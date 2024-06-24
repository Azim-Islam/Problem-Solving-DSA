

for _ in range(int(input())):
    R, C, I = map(int, input().split())
    arr = [["."]*C for bl in range(R)]
    for m in range(I):
        r1, c1, r2, c2, char = input().split()
        r1 = int(r1)
        c1 = int(c1)
        r2 = int(r2)
        c2 = int(c2)
        for i in range(r1-1, r2):
            for j in range(c1-1, c2):
                arr[i][j] = char

    [print(*i, sep='') for i in arr]
