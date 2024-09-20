from math import sqrt

def dd(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + (y1-y2)**2)

for _ in range(int(input())):
    n = int(input())
    # a, b = map(int, input().split())
    # f = True
    points = []
    for __ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    
    x1, y1, x2, y2 = map(int, input().split())
    
    ab = dd(x1, y1, x2, y2)
    
    for x, y in points:
        ac = dd(x1, y1, x, y)
        bc = dd(x2, y2, x, y)
        # print(ab, ac, bc)
        if ab >= bc:
            print("NO")
            break
    else:
        print("YES")