from collections import defaultdict
n = int(input())
arr = list(input())
    
c = len(set(arr))
ans = float('inf')
j = 0
d = defaultdict(int)
    
for i in range(n):
    while j < n:
        if len(d) == c:
            ans = min(ans, abs(i-j+1))
            break
        else:
            d[arr[j]] += 1
            j += 1
    if len(d) == c:
        ans = min(ans, abs(i-j+1))
    d[arr[i]] -= 1
    if not d[arr[i]]:
        d.pop(arr[i])
    
print(ans+1)
    