def forward_pass(arr):
    dp = [0, abs(arr[0]-arr[1])] #Cost to visit the 0th, 1st node

    for i in range(2, n):
        v1 = abs(arr[i-1]-arr[i]) + dp[i-1]
        v2 = abs(arr[i-2]-arr[i]) + dp[i-2]
        dp.append(min(v1,v2))
    return dp[-1]
n = int(input())
arr = list(map(int, input().split()))
print(forward_pass(arr))