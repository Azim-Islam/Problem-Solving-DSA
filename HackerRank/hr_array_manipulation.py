def arrMan(i, j, v, array):
    for k in range(i, j):
        array[k] += v
n, m = map(int, input().split())
array = [0]*n
for _ in range(m):
    i, j, v = map(int, input().split())
    arrMan(i-1, j, v, array)
print(max(array))