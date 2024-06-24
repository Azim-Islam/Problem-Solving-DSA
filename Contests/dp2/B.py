import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = sorted(set(map(int, input().split())))

dp = [0]*(k+1)

for i in range(1, k+1):
    tmp = []
    for j in arr:
        if j > i:
            break
        tmp.append(dp[i-j])
    if 0 in tmp:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[k] == 1:
    print("First")
else:
    print("Second")