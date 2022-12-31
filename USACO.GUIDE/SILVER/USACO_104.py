import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr_info = [0]*(n+1)
for _ in range(k):
    l, r = map(int, input().split())
    arr_info[l-1] += 1
    arr_info[r] -= 1

cum_sum = [0]*(n+1)
s = 0
for i in range(n):
    s = s + arr_info[i] 
    cum_sum[i] += s
    
    
cum_sum.sort()
print(cum_sum[n//2 + 1])