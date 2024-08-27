def solve(x, k, parr, arr):
    ans = 0
    ans2 = 0
    kk = k
    while k and kk-k <= len(arr):
        ans = max(ans, ans2 + k*(arr[x-1]))
        ans2 = ans2+arr[x-1]
        x = parr[x-1]
        k -= 1
        # print(k)
    return max(ans, ans2)

for _ in range(int(input())):
    n, k, b, s = map(int, input().split())
    parr = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    ans1 = solve(b, k, parr, arr)
    ans2 = solve(s, k, parr, arr)

    if ans1 > ans2:
        print("Bodya")
    elif ans1 < ans2:
        print("Sasha")
    else:
        print("Draw")