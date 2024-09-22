import gc
gc.disable()
import sys




input = sys.stdin.readline
def solve():
    for _ in range(int(input())):
        n, k  = map(int, input().split())
        arr = list(map(int, input().split()))

        gold = 0
        c = 0
        for i in arr:
            if i >= k:
                gold += i
            elif gold and not i:
                c += 1
                gold -= 1
        print(c)

solve()