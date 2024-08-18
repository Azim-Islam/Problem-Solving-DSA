for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    suff = [0]*(n+1)

    suff[n-1] = arr[n-1]

    for i in range(n-2, -1, -1):
        if arr[i] > suff[i+1]:
            suff[i] = arr[i]
        else:
            suff[i] = suff[i+1]+1

    print(suff[0])