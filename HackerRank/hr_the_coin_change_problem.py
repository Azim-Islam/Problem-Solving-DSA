# https://www.hackerrank.com/challenges/coin-change/problem
# points - 60

from functools import lru_cache
n, m = map(int, input().split())
coins = list(map(int, input().split()))

coins.sort()
count = 0
calls = 0

@lru_cache(None)
def coinChange(change, index):

    if change == 0:
        #print(f"Current change:{change}, Current Note:{coins[index]}")
        #print(count)
        return 1
    if change < 0 or index >= m or coins[index] > change:
        #print("Failed", f"Current change:{change}, Current Note:")
        return 0
    else:
        #print(f"Current change:{change}, Current Note:{coins[index]}")
        return coinChange(change, index + 1) + coinChange(change - coins[index], index)
        
        
answer = coinChange(n, 0)

print(answer)