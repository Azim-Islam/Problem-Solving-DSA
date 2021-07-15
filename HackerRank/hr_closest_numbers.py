n = int(input())
array = sorted(map(int, input().split()))
diff = 999999
pairs = []
for i in range(len(array)-1):
    if abs(array[i]-array[i+1]) < diff:
        diff = abs(array[i]-array[i+1])
        pairs = [array[i], array[i+1]]
    elif abs(array[i]-array[i+1]) == diff:
        pairs.append(array[i])
        pairs.append(array[i+1])
print(*pairs)