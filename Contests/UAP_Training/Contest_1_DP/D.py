from collections import deque
import gc

gc.enable()
def memoize(values, weights, n, w):
    dp = deque([[weights[0] if values[0]==i else float('inf') for i in range(10**5+1)]])
    dp[0][0] = 0
    for i in range(1, n):
        dp.append([0]*(10**5+1)) # [0000000000]
        for j in range(1, 10**5+1):
            prev_cost = dp[0][j]
            k = (j-values[i]) if j - values[i] >= 0 else 0
            curr_cost = dp[0][k] + weights[i]
            dp[1][j] = min(prev_cost, curr_cost)
        dp.popleft()
        gc.collect()
    for i in range(10**5, -1, -1):
        if dp[-1][i] <= w:
            print(i)
            break
            


n, k = map(int, input().split())
values = [0]*n
weights = [0]*n

for i in range(n):
    w, v = map(int, input().split())
    values[i] = v
    weights[i] = w

memoize(values, weights, n, k)