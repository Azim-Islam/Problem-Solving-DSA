import gc
gc.disable()
import sys




input = sys.stdin.readline

def pp(n):
    return (n*(n+1))//2

def solve():
    for _ in range(int(input())):
        # n = int(input())
        n, k = map(int, input().split())
        ss = pp(n) - pp(n-k)


        if ss%2:
            print("NO")
        else:
            print("YES")


solve()