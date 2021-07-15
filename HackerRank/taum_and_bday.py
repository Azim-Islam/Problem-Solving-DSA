for _ in range(int(input())):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    ans1 = w*wc + (wc+z)*b
    ans2 = w*(bc+z) + bc*b
    ans3 = w*wc + b*bc
    print(min(ans3, (min(ans1, ans2))))