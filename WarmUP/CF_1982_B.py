for _ in range(int(input())):
    x, y, k = map(int, input().split())
    x += 1
    k -= 1
    while x%y == 0:
        x = x//y

    while k >= ((x+y-1)//y)*y - x:
        k -= ((x+y-1)//y)*y - x
        x = (x+((x+y-1)//y)*y - x)
        while x%y == 0:
            x = x//y

        if x == 1:
            k = (k%(y-1))
            break
        
        # print(x, y, k)
    print(x+k)