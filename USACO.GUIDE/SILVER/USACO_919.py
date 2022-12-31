input = open('paintbarn.in', 'r').readline
fout = open('paintbarn.out', 'w')

n, k = map(int, input().split())
arr = [[0 for x in range(1002)] for y in range(1002)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 1
    y1 += 1
    x2 += 1
    y2 += 1
    arr[x1][y1] += 1
    arr[x2][y2] += 1
    arr[x1][y2] -= 1
    arr[x2][y1] -= 1

ans = 0
for i in range(1, 1002):
    for j in range(1, 1002):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
        if arr[i][j] == k:
            ans += 1
# print(*arr, sep="\n")
print(ans, file=fout)