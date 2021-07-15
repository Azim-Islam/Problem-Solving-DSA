def quicksort(p, *array):
    pivot = int(p)
    #print(pivot, str(pi))
    left, right = [], []
    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    if len(left) > 1:
            left = quicksort(*left)
            print(*left)
    if len(right) > 1:
            right = quicksort(*right)
            print(*right)
    return left+[pivot]+right
    
n = int(input())
pivot, *arr = map(int, input().split())
print(*quicksort(pivot, *arr))