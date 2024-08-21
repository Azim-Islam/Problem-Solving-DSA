from math import ceil

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, list(input())))
    one = sum(arr)
    zero = 0
    ans = 0
    m = n
    if ceil((n-(0))/2) <= one and ceil((0)/2) <= zero:
        m = n/2
        ans = 0
    for i in range(0, n):
        if arr[i] == 1:
            one -= 1
        if arr[i] == 0:
            zero += 1
        if ceil((n-(i+1))/2) <= one and ceil((i+1)/2) <= zero:
            if abs(n/2 - (i+1)) < m:
                ans = i+1
                m = abs(n/2 - (i+1))
        # print(ceil((i+1)/2), ceil((n-(i+1))/2), zero, one, i+1)
    print(ans) 
