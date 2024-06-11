for _ in range(int(input())):
    n, m = map(int, input().split())
    MAP = []
    for i in range(n):
        MAP.append(list(input()))

    min_y = float('inf')
    max_y = float('-inf')

    for x in range(n):
        for y in range(m):
            if MAP[x][y] == "#":
                min_y = min(min_y, y+1)
                max_y = max(max_y, y+1)
    
    min_x = float('inf')
    max_x = float('-inf')
    for y in range(m):
        for x in range(n):
            if MAP[x][y] == "#":
                min_x = min(min_x, x+1)
                max_x = max(max_x, x+1)


    print((min_x+max_x)//2, (min_y+max_y)//2)