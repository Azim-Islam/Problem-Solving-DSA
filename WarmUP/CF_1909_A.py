def solve(arr, reverse):
    arr.sort()
    U = False
    D = False
    L = False
    R = False
    

    x, y = 0, 0 
    # arr.sort(reverse=reverse)
    for i, j in arr:
        if j > y:
            U = True
        if j < y:
            D = True 
        y = j
        if i > x:
            R = True
        if i < x:
            L = True
        x = i

    
    if U and D and L and R:
        return False
    return True

for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr1 = [[j, i] for i, j in arr]
    if solve(arr, False) or solve(arr, True) or solve(arr1, False) or solve(arr1, True):
        print("YES")
    else:
        print("NO")