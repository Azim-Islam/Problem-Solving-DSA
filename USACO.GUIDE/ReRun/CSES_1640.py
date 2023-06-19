from sys import stdin
from collections import defaultdict

input = stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# d = defaultdict(int)
# 
# for i, v in enumerate(arr):
#     d[v] = i
#     
# for i, v in enumerate(arr):
#     tmp = str(x - int(v))
#     if tmp in d and d[tmp] != i:
#         print(i+1, d[tmp]+1)
#         break
# else:
#     print("IMPOSSIBLE")

arr = sorted(enumerate(arr), key=lambda x: x[1])
i = 0
j = n - 1

while i < j:
    if arr[i][1] + arr[j][1] == x:
        print(arr[i][0]+1, arr[j][0]+1)
        break
    elif arr[i][1] + arr[j][1] > x:
        j -= 1
    elif arr[i][1] + arr[j][1] < x:
        i += 1
else:
    print("IMPOSSIBLE")