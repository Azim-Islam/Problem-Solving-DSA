for _ in range(int(input())):
    n = int(input())
    # arr = list(map(int, input().split()))
    string = "aeiou"
    ans = []
    for i in range(n):
        ans.append(string[i%len(string)])

    ans.sort()
    print("".join(ans))