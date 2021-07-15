n = int(input())
array = sorted(map(int, input().split()), reverse=True)
i = 0
flag = 1
while i+2<n:
    if array[i] < array[i+1] + array[i+2]:
        print(array[i+2], array[i+1], array[i])
        flag = 0
        break
    else:
        i += 1
print("-1"*flag, end="")