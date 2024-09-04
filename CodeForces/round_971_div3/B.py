for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(n):
        line = list(input())
        for i, v in enumerate(line):
            if v == "#":
                ans.append(i+1)
    print(*ans[::-1])