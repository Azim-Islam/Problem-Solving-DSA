for _ in range(int(input())):
    n, m, sx, sy, d = map(int, input().split())
    #traverse both ways
    #column traverse
    cc = 0
    for i in range(2, n+1):
        if abs(sx-i)+abs(sy-1) <= d:
            cc = float('inf')
            break
        else:
            cc += 1
    for i in range(2, m+1):
        if abs(sx-n)+abs(sy-i) <= d:
            cc = float('inf')
            break
        else:
            cc += 1
    #row traverse
    cr = 0
    for i in range(2, m+1):
        if abs(sx-1)+abs(sy-i) <= d:
            cr = float('inf')
            break
        else:
            cr += 1
    for i in range(2, n+1):
        if abs(sx-i)+abs(sy-m) <= d:
            cr = float('inf')
            break
        else:
            cr += 1
    if cr == float('inf') and cc == float('inf'):
        print('-1')
    else:
        print(min(cr, cc))
    # print(cr, cc)