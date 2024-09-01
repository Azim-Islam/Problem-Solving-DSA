for _ in range(int(input())):
    a, b = map(int, input().split())
    if (a%2) == 0 and b%2 == 0:
        print("YES")
    elif b%2 and a-2 >= 0 and (a-2)%2 == 0:
        print("YES")
    else:
        print("NO")
    