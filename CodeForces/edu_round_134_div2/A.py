for _ in range(int(input())):
    pxl = list(input())
    pxl += list(input())
    print(len(set(pxl))-1)