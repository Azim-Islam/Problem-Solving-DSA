for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_diff = 0
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1]) 
        if diff > 1:
            sum_diff += diff
        if sum_diff > 4 or diff > 3:
            print("NO")
            break
    else:
        print("YES")
    # if n == 1:
    #     print("YES")