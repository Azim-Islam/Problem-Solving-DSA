def search(array, money):
    i, j = 0, len(array)-1
    while 1:
        val = array[i][1] + array[j][1]
        if val > money:
            j -= 1
        elif val < money:
            i += 1
        else:
            print(*sorted([array[i][0]+1, array[j][0]+1]))
            break
for _ in range(int(input())):
    m = int(input())
    n = int(input())
    array = list(map(int, input().split()))
    array = list(enumerate(array))
    array = sorted(array, key=lambda x: x[1])
    search(array, m)