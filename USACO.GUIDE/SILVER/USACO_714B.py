from bisect import bisect_left as bl, bisect_right as br

input = open("helpcross.in", 'r').readline
fout = open("helpcross.out", 'w')

C, N = map(int, input().split())

arr = list()
cows = list()


for _ in range(C):
    arr.append(int(input()))


arr.sort()

for _ in range(N):
    cows.append(list(map(int, input().split())))

cows.sort(key=lambda x: x[1])

ans = 0

for x, y in cows:
    start = bl(arr, x)
    end = br(arr, y)
    if start == end:
        pass
    else:
        c += 1
        del arr[start]

print(c, file=fout)