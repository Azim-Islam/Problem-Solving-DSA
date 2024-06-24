from functools import lru_cache
# @lru_cache(None)
def search(dp, ans, max_, s, t, i, j):
    print(i, j)
    if i == 0 or j == 0:
        return []
    elif (i > 1 and j > 1) and s[j-1] == t[i-1]:
        print(s[j-1])
        ans.append(s[j-1])
        if len(ans) == max_:
            print(ans)
        else:
            search(dp, ans, max_, s, t, i-1, j-1)
    else:
        search(dp, ans, max_, s, t, i, j-1)
        search(dp, ans, max_, s, t, i-1, j)

     

def solve(s, t):
    dp = [[0]*(len(s)+1)]
    for i in range(1, len(t)+1):
        dp.append([0]*(len(s)+1))
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] += dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #Backward pass
    # i = len(t)
    # j = len(s)
    # ans = []
    # while(i > 0 and j > 0):
    #     if s[j-1] == t[i-1]:
    #         ans.append(s[j-1])
    #         i -= 1
    #         j -= 1
    #     elif dp[i-1][j] > dp[i][j-1]:
    #         i -= 1
    #     else:
    #         j -= 1
    print(dp[-1][-1])
    ans = search(dp, [], dp[-1][-1], s, t, len(t), len(s))

    # print(ans)
    print("".join([ans[i] for i in range(len(ans)-1, -1, -1)]))

s = list(input())
t = list(input())

solve(s, t)