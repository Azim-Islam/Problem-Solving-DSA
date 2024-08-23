from collections import defaultdict

cache = defaultdict(int)

def hishab(x):
    if cache[x]:
        return cache[x]
    count = 0
    t = x
    while x:
        x = x//3
        count += 1
    cache[t] = count
    return count


dp = [0]*(2*10**5+1)
for i in range(1, 2*10**5+1):
    dp[i] = dp[i-1] + hishab(i)

for _ in range(int(input())):
    x, y = map(int, input().split())
    c = hishab(x) ; 
    # print(c)
    c *= 2

    print(c + dp[y]-dp[x])