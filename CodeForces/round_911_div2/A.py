for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    c = 0
    for i in range(n):
        if s[i] == ".":
            c += 1
            ans += 1
            if c > 2:
                ans = 2
                break
        elif s[i] == "#":
            c = 0
    
    print(ans)
