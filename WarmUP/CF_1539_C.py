import gc
gc.disable()
import sys
input = sys.stdin.readline

def solve():
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    pos = []
    for i in range(n-1):
        if arr[i+1]-arr[i] > x:
            pos.append([arr[i+1], arr[i]])

    # print(pos)
    pos.sort(key=lambda x: x[0]-x[1])
    # print(pos)
    g = len(pos) + 1

    for i, j in pos:
        vv = ((i-j+x-1)//x)-1
        if k and vv <= k:
            k -= vv
            g -= 1

    print(g, file=sys.stdout)

solve()