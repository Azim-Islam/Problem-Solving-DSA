for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(0, n):
        if i%2:
            arr.append(i)
        else:
            arr.append(i+2)
    if n%2:
        arr[-1], arr[-2] = arr[-2], arr[-1] 
        arr[-2] -= 1
    print(*arr)