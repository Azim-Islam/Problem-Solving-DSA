t = int(input())

def check(arr, w, x, y, m):
    for a, b, c in arr:
        if x*a + y*b > c:
            if a!=b:
                # Y = (c - a*w)//(b-a)
                X = (c - b*(m-w))//(a-b)
                if 0 < X <= x and 0 < w - X <= y:
                    x = X
                    y = w - x
                # elif 0 < Y <= y and 0 < w - Y <= x:
                #     x = w - Y
                #     y = Y
                #     print(w, x, y)
                else:
                    return 0
            else:
                z = a+b
                if z*(m-w) <= c:
                    pass
                else:
                    
                    return 0
    return 1

for _ in range(t):
    input()
    n, c, m = map(int, input().split()) 
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    #Binary Search
    hi = c+m
    lo = 2

    x = c
    y = m

    while lo < hi:
        mid = (lo + hi)//2

        ans = check(arr, mid, x, y, c+m)
        if ans:
            hi = mid
        else:
            lo = mid+1


    print(hi)
        