def check(a, b, c, d):
    if a >= c and b >= c:
        return True
    if a <= d and b <= d:
        return True
    if c >= a >= d and c >= b >= d:
        return True
    return False



for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, b = max(a, b), min(a, b)
    c, d = max(c, d),  min(c, d)
    if check(a, b, c, d) or check(c, d, a, b):
        print("NO")
    else:
        print("YES")