from sys import stdin

def arrMan(i, j, v, array):
    array[i] += v
    array[j+1] -= v
    

n, m = map(int, input().split())

maxval = 0
cval = 0

array = [0]*(n+2)

for _ in range(m):
    i, j, v = map(int, stdin.readline().split())
    arrMan(i, j, v, array)

for i in array:
    cval += i
    if cval > maxval:
        maxval = cval

print(maxval)