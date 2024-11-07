for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    under_rows = n - r
    moved = under_rows*m + (m-c)
    total = moved + (m-1)*under_rows
    print(total)
