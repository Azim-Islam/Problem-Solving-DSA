for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
        print("NO")
    else:
        print("YES")