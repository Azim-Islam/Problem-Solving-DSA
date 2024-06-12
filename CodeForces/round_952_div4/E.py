def gt(arr, v):
    if arr[0] >= v[0] and arr[1] >= v[1] and arr[2] >= v[2]:
        return 1
    return 0

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = arr.pop()
    arr.sort()
    
    
    ans = 0
    for i in range(1, arr[-1]+1):
        for j in range(1, arr[-2]+1):
            if k%(i*j) == 0:
                v = [i, j , k//(i*j)]
                v.sort()
                if gt(arr, v):
                    ans = max(ans, (arr[0]-v[0]+1)*(arr[1]-v[1]+1)*(arr[2]-v[2]+1))
                    # print(ans)

    print(ans)