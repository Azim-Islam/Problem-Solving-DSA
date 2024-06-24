def memoize(values, weights, n, w):
    dp = [[values[0] if (i - weights[0]>=0) else 0 for i in range(w+1)]]
    for i in range(1, n):
        dp.append([0]*(w+1))
        for j in range(w+1):
            dp[i][j] = max(dp[i-1][j], (values[i] if j - weights[i]  >= 0 else 0) + dp[i-1][max(0, j - weights[i])])
    return dp[-1][-1]



n, w = map(int, input().split())
values = [0]*n
weights = [0]*n


for i in range(n):
    p, v = map(int, input().split())
    values[i] = v
    weights[i] = p

print(memoize(values, weights, n, w))