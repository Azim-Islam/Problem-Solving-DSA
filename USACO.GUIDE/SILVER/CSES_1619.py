import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
arr = []
points = []

def compIdx(arr, i):
    return bisect_right(arr, i) - 1

for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])
    points.append(s)
    points.append(e)

points.sort()
diff_arr = [0]*len(points)

for s, e in arr:
    diff_arr[compIdx(points, s)] += 1
    diff_arr[compIdx(points, e)] -= 1


for i in range(1, len(diff_arr)):
    diff_arr[i] = diff_arr[i-1] + diff_arr[i]

print(max(diff_arr))