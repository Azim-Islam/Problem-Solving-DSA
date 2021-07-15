def binarySearch(array, n):
    i, j = 0, len(array)-1
    while 1:
        if array[(i+j)//2] < n:
            i = (i+j)//2
        elif array[(i+j)//2] > n:
            j = (i+j)//2
        else:
            if array[(i+j)//2] == n:
                print(f"Found N in index {(i+j)//2}")
                break
            else:
                print("Found nothing")
                break
array = [i for i in range(1, 21)]
print(array, "\nSelect your number")
n = int(input())
binarySearch(array, n)