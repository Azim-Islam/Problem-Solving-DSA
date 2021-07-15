
def larrysArray(array):
    k = 0
    lenght = len(array)
    while k < lenght:
        i = 0
        while i < lenght - 2:
            li = array[i:i+3]
            array[i:i+3] = min(array[i:i+3], [li[1],li[2],li[0]], [li[2],li[0],li[1]])
            i += 1
        k += 1
    #print(array)
    if array == sorted(array):
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    larrysArray(array)

