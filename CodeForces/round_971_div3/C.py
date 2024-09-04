for _ in range(int(input())):
    # n = int(input())
    x, y, k = map(int, input().split())
    mx = (x+k-1)//k
    my = (y+k-1)//k
    ans = max(mx, my)*2
    if mx > my:
        ans -= 1
    print(ans)