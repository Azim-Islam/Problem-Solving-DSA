for _ in range(int(input())):
    n = int(input())
    arr = []
    j = 0
    for i in range(n-1, 0, -1):
        if sum(arr) + i < n:
            arr.append(i)
        else:
            j = i
            break
    arr2 = [i for i in range(1, j+1)]
    ans = arr2[::-1]+arr[::-1]+[n] 
    if n%2:
        ans[0], ans[1] = ans[1], ans[0]
    print(*ans)