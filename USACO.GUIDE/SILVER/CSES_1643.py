n = int(input())
arr = list(map(int, input().split()))

mss = []

s = 0
for i in arr:
    mss.append(max(0, s+i))
    s = max(0, s+i)

ans = 0
if max(mss) == 0:
    print(max(arr))
else:
    print(max(mss))