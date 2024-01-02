import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])
first = arr[0][1]
c = 1
for x in arr[1:]:
    if x[0] >= first:
        c += 1
        first = x[1]
print(c)