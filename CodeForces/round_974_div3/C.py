import gc
gc.disable()
import sys




input = sys.stdin.readline
def check(n, arr, x):
    arr[-1] += x
    ss = sum(arr)
    avg = ss/(n*2)
    unhappy = 0
    for i in range(n):
        if arr[i] < avg:
            unhappy += 1
    arr[-1] -= x
    # print(unhappy, x)
    if unhappy > n/2:
        return True
    return False        


def solve():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        lo = 0
        hi = 10**14
        while lo < hi:
            mid = (hi+lo)//2
            if check(n, arr, mid):
                hi = mid
            else:
                lo = mid + 1

        if hi != 10**14:
            print(hi)
        else:
            print("-1")

solve()