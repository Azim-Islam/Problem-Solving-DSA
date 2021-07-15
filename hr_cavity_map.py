#cell is not on the border of the map
#each cell adjacent to it has strictly smaller depth (a<b)
twoD_map = []
x_s = []
n = int(input())
for i in range(n):
    twoD_map.append(list(map(int, input())))
if n<2:
    [print(*i, sep='') for i in twoD_map]
    quit()
for i in range(1, n-1):
    for j in range(1, n-1):
        if (twoD_map[i][j] > twoD_map[i+1][j]) and (twoD_map[i][j] > twoD_map[i-1][j]) and (twoD_map[i][j] > twoD_map[i][j+1]) and (twoD_map[i][j]> twoD_map[i][j-1]):
            x_s.append([i,j])
for i in x_s:
    x,y = i[0], i[1]
    twoD_map[x][y] = 'X'
[print(*i, sep='') for i in twoD_map]