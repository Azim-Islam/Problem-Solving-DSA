def bigSort(array):
    return array.sort(key=lambda x: (len(x), x))


array = []

for _ in range(int(input())):
    array.append(input())

bigSort(array)

print(*array, sep="\n")
