array = [0]*101
n = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    array[i] = 1^array[i]
for i in range(len(array)):
    if array[i] == 1:
        print(i)
        break