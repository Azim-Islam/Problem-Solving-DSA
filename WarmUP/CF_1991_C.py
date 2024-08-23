for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    avg = 2**30
    for i in range(40):
        avg = avg//2
        for j in range(n):
            arr[j] = abs(arr[j]-avg)
        ans.append(avg)        
        if all(arr) and sum(arr) == n:
            print(len(ans)+1)
            print(*ans, 1)
            break
    else:
        print(-1)