n = int(input())
array = list(map(int, input().split()))
array.sort()

min_unit = array[0]
count = 1

for i in range(len(array)):
    if array[i] > min_unit + 4:
        count += 1
        min_unit = array[i]

print(count)