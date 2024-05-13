def check(x1, y1, x2, y2, time, s):
    wind_x = 0
    wind_y = 0

    for c in s:
        if c == "U":
            wind_y += 1
        if c == "D":
            wind_y -= 1
        if c == "L":
            wind_x -= 1
        if c == "R":
            wind_x += 1

    wind_x *= time//len(s)
    wind_y *= time//len(s)

    for i in range(time%len(s)):
        c = s[i]
        if c == "U":
            wind_y += 1
        if c == "D":
            wind_y -= 1
        if c == "L":
            wind_x -= 1
        if c == "R":
            wind_x += 1

    x1 += wind_x
    y1 += wind_y
    return abs(x1 - x2) + abs(y1 - y2) <= time

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
s = list(input())

lo = 1
hi = 10**15
valid = -1

while lo < hi:
    mid = (lo+hi)//2
    if check(x1, y1, x2, y2, mid, s):
        valid = mid
        hi = mid
    else:
        lo = mid + 1

print(valid)