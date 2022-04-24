from functools import lru_cache
import sys
sys.setrecursionlimit(10**5)

m = 1000000007
def G(x):
    if x == 0:
        return 2
    elif x == 1:
        return 1
    ans = (2*G_dict[x-1]%m + G_dict[x-2]%m)%m
    G_dict[x] = ans
    return ans

def cache_extras(y):
    for i in range(y+1):
        G_dict[i] = G(i)
        

def F(x):
    ans = 0
    if x == 0:
        return 2

    ans = (F_dict[x-1]%m + G_dict[M*(x-1)]%m)%m
    F_dict[x] = ans
    
    return ans


G_dict = {0: 2, 1:1}
for _ in range(int(input())):
    x, M = map(int, input().split())
    F_dict = {0: 2}
    ans = 0
    cache_extras((M*(x-1))%m)
    for i in range(x+1):
        ans = F(i)
    print(f"Input {bin(x)} Case {_+1}: {bin(ans)}")
    F_dict.clear()