for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = ["B"]*m
    for i in range(len(arr)):
        index = min((m-arr[i]), arr[i]-1)
        if s[index] == "B":
            s[index] = "A"
        else:
            index = max((m-arr[i]), arr[i]-1)
            s[index] = "A"
    print("".join(s))