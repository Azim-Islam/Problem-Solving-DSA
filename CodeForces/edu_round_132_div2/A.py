from ssl import OP_ENABLE_MIDDLEBOX_COMPAT


for _ in range(int(input())):
    x = int(input())
    arr = list(map(int, input().split()))
    opened = [0]*4
    opened[x] = 1
    opened[arr[x-1]] += 1
    x = arr[x-1]
    opened[arr[x-1]] += 1
    x = arr[x-1]
    if opened[1:].count(1) == 3:
        print("YES")
    else:
        print("NO")