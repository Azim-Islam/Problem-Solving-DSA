for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(2*n):
        arr.append(list(map(int, input().split())))
    
    selection = []
    for i in range(n):
        for j in range(n):
            maxx = max([arr[i][j], arr[i][2*n-1-j], arr[2*n-1-i][j], arr[2*n-1-i][2*n-1-j]])
            selection.append(maxx)

    print(sum(selection))
