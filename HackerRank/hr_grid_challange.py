for _ in range(int(input())):
    grid = []
    n = int(input())
    for i in range(n):
        grid.append(sorted(input()))
    flag = 1
    n = len(grid[0])
    for x in range(n):
        for y in range(n-1):
            if grid[y][x] > grid[y+1][x]:
                flag = 0
                print("NO")
                break
        if not flag:
            break
    else:
        print("YES")