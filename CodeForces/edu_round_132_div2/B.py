import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cost_arr_f = [0]*n
cost_arr_b = [0]*n

for i in range(1, n):
    cost = max(arr[i-1]-arr[i], 0)
    cost_arr_f[i] += cost_arr_f[i-1] + cost
# print(cost_arr_f)

for i in range(n-2, -1, -1):
    cost = max(arr[i+1]-arr[i], 0)
    cost_arr_b[i] += cost_arr_b[i+1] + cost

for j in range(m):
    s, t = map(int, input().split())
    ans = 0
    if t > s:
        print(abs(cost_arr_f[s-1]-cost_arr_f[t-1]))
    else:
        print(abs(cost_arr_b[s-1]-cost_arr_b[t-1]))