
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n-1):
        r, m, l = arr[i-1], arr[i]//2, arr[i+1]

        kom = min([r, m, l])
        arr[i-1] -= kom
        arr[i] -= kom*2
        arr[i+1] -= kom

    flag = 1
    for i in arr:
        if i: flag = 0
        
    if flag:
        print("YES")
    else:
        print("NO")    
