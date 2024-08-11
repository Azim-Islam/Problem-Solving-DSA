from math import ceil, sqrt

input = open('moocast.in', 'r').readline
out = open('moocast.out', 'w')




## check
def check(arr, dist):
    #DFS
    count = 1
    visited = [0]*len(arr)
    stack = [0]
    visited[0] = 1
    f = True
    while stack:
        i = stack.pop()
        x1, y1 = arr[i]
        for j in range(len(arr)):
            x2, y2 = arr[j]
            if not visited[j] and dist >= (x1-x2)**2 + (y1-y2)**2 :
                stack.append(j)
                visited[j] = 1
                count += 1
                f = False
        if f:
            return False

    if count == len(arr):
        return True
    else:
        return False

def solve():
    n = int(input())
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    hi = 25_000*25_000
    lo = 0
    while lo < hi:
        mid = (hi+lo)//2
        if check(arr, mid):
            hi = mid
        else:
            lo = mid + 1
    
    
    print(hi, file=out)
    # print(hi)
solve()