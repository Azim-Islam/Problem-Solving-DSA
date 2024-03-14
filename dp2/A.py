import sys

input = sys.stdin.readline

n = int(input())

arr = []
a = 0
b = 0

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

if arr[0][0]:
    a = max(0, arr[0][1])
else:
    b = max(0, arr[0][1])

for x, v in arr[1:]:
    if x: # x is poisonous
        a = max(a, b+v)
    else: # x is not poisonous
        b = max([b, a+v, b+v])

print(max(a, b))