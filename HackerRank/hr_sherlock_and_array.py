def arraySearch(array):
    left_sum = 0
    right_sum = 0
    i = -1
    j = len(array)
    
    while j-i > 2:
        if left_sum == right_sum:
            if array[i+1] < array[j-1]:
                i += 1
                left_sum += array[i]
            else:
                j -= 1
                right_sum += array[j]

        elif left_sum < right_sum:
            i += 1
            left_sum += array[i]
        else:
            j -= 1
            right_sum += array[j]
        #print(left_sum, right_sum)

    if left_sum == right_sum:
        print("YES")
    else:
        print("NO")
        
for _ in range(int(input())):
    n = input()
    array = list(map(int, input().split()))
    arraySearch(array)