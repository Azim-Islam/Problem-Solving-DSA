def check(arr):
    c = 0
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            c += 1
    return c


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mm = float('inf')
    a, b = 0, 1
    for i in range(n-1):
        if arr[i+1]-arr[i] < mm:
            mm = min(mm, arr[i+1]-arr[i])
            a, b = i, i+1

    new_arr = [arr[a]]


    for i in range(b+1, n):
        new_arr.append(arr[i])
    
    for i in range(0, a):
        new_arr.append(arr[i])
        
    new_arr.append(arr[b])

    print(*new_arr)