n = int(input())
 
hi = n*n
lo = 0
 
while hi - lo > 1:
    mid = (hi + lo)//2
 
    t = 0
    for i in range(1, n+1):
        t += min(n, mid//i)
        
    if t < ((n*n)+1)//2:
        lo = mid
    else:
        hi = mid 
 
print(hi)