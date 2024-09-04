for _ in range(int(input())):
    # n = int(input())
    a, b = map(int, input().split())
    ans = float('inf')
    for i in range(a, b+1):
        ans = min(ans, (i-a)+(b-i))

    print(ans)