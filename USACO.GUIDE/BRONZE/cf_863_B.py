from collections import Counter, deque
    
n = int(input())
arr = list(map(int, input().split()))
    
def findsol(barr):
    barr = sorted(barr)
    d = 0
    for i in range(0, len(barr), 2):
    # print(arr[i], arr[i+1])
        d += abs(barr[i] - barr[i+1])
    # print(barr)
    return d
    
sol = float('inf')
for i in range(n*2):
    t1 = arr[0] 
    del arr[0]
    for j in range(n*2):
        t2 = arr[0]
        del arr[0]
        sol = min(sol, findsol(arr))
        arr.append(t2)
    arr.append(t1)
    
print(sol)