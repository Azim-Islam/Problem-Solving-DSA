import sys
from math import gcd


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

pref_sum = [0]*n
pref_sum[0] = arr[0]

suf_sum = [0]*n
suf_sum[n-1] = arr[n-1]

ans = 0

for i in range(1, n):
    pref_sum[i] = gcd(arr[i], pref_sum[i-1])

for i in range(n-2, -1, -1):
    suf_sum[i] = gcd(suf_sum[i+1], arr[i])


for i in range(1, n-1):
    ans = max(ans, gcd(suf_sum[i+1], pref_sum[i-1]))

ans = max(ans, suf_sum[1])
ans = max(ans, pref_sum[n-2])

print(ans)