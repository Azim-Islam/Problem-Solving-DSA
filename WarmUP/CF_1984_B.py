for _ in range(int(input())):
    n = int(input())
    l = len(str(n))
    new = "9"*(l-1)
    other = str(n - int("".join(new)))
    # print(new, other, end=" ")
    f = True
    if len(new) != len(other):
        f = False
    for c1, c2 in zip(new, other):
        c1 = int(c1)
        c2 = int(c2)
        if c2 - 5 >= 0:
            pass
        elif abs(c2 - 5) <= 4:
            pass
        else:
            f = False
            break
    if f:
        print("YES")
    else:
        print("NO")

