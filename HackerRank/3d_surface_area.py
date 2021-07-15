H, W = map(int, input().split())
array = []
area = 0
for i in range(H):
    array.append(list(map(int, input().split())))
for i in range(H):
    for j in range(W):
        area += array[i][j]*4+2
        if j+1 < W and array[i][j+1] >= array[i][j]:
            area -= array[i][j]
        if j-1 > -1 and array[i][j-1] >= array[i][j]:
            area -= array[i][j]
        if i+1 < H and array[i+1][j] >= array[i][j]:
            area -= array[i][j]
        if i-1 > -1 and array[i-1][j] >= array[i][j]:
            area -= array[i][j]
            
        if j+1 < W and array[i][j+1] < array[i][j]:
            area -= array[i][j+1]
        if j-1 > -1 and array[i][j-1] < array[i][j]:
            area -= array[i][j-1]
        if i+1 < H and array[i+1][j] < array[i][j]:
            area -= array[i+1][j]
        if i-1 > -1 and array[i-1][j] < array[i][j]:
            area -= array[i-1][j]
print(area)