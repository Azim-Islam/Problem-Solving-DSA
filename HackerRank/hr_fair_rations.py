# Input > array = [3, 4, 5, 6, 7, 8, 10]
# custom test = [4, 5, 9]
def fairRations(array):
    breads = 0
    for i in range(0, len(array)-1):
        if array[i] % 2 == 1:
            array[i] += 1
            if i and array[i-1]%2 == 1:
                array[i-1] += 1
            else:
                array[i+1] += 1
            breads += 2
    sum1 = sum(array)%2
            
    if sum1:
        print("NO")
    else:
        print(breads)


n = input()
array = list(map(int, input().split()))
fairRations(array)
