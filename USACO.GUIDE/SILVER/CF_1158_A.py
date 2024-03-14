import sys

input = sys.stdin.readline

def solve(arr_f, arr_g):
    mx = arr_f[-1]
    s = sum(arr_f)
    ans = 0
    for v in arr_g:
        ans += s + (v-mx)
    if mx in arr_g:
        print(ans)
    else:
        ans -= s + (arr_g[0] - mx)
        ans += s + (arr_g[0] - arr_f[-2])
        print(ans)


n, m = map(int, input().split())

arr_f = list(map(int, input().split()))
arr_g = list(map(int, input().split()))

arr_f.sort()
arr_g.sort()


if arr_f[-1] > arr_g[0]:
    print("-1")
else:
    solve(arr_f, arr_g)