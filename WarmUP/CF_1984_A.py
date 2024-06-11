for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] == arr[-1]:
        print("NO")
    else:
        print("YES")
        s = list("R"*n)
        s[n//2] = 'B'
        print("".join(s))