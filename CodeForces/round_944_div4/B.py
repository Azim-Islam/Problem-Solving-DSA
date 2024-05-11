for _ in range(int(input())):
    s = list(input())
    r = s[:]
    for i in range(10):
        r = [r.pop()] + r
        if s != r:
            print("YES")
            print("".join(r))
            break
    else:
        print("NO")