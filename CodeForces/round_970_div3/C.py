from bisect import bisect_left

nn = lambda x: (x*(x+1))//2
dp = [0]*(10**5+1)
for i in range(10**5+1):
    dp[i] = nn(i)

# print(dp)
for _ in range(int(input())):
    l, r = map(int, input().split())
    v = r-l
    idx = bisect_left(dp, v)
    if dp[idx] > v:
        print(idx)
    else:
        print(idx+1)