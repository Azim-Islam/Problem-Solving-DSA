from bisect import bisect_right as br

n = int(input())

arr = list(map(int, input().split()))

towers = []

for v in arr:
    idx = br(towers, v)
    if idx == len(towers):
        towers.append(v)
    else:
        towers[idx] = v

print(len(towers))