for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x,y))
    #x axis positive max
    xp = 0
    yp = 0
    yn = 0
    xn = 0
    for i in arr:
        if i[0] > 0:
            xp = max(xp, i[0])
        if i[1] > 0:
            yp = max(yp, i[1])
        if i[0] < 0:
            xn = min(xn, i[0])
        if i[1] < 0:
            yn = min(yn, i[1])

    dist = xp + yp + xp + abs(xn) + yp + abs(yn) + abs(xn) + abs(yn)
    print(dist)