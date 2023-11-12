arr = [i for i in range(1, 101)]
for _ in range(int(input())):
    n = int(input())
    interval = []
    ans = 0
    for i in arr:
        if n%i == 0:
            if interval and interval[-1]+1 != i:
                ans = max(ans, interval[-1]-interval[0]+1)
                interval = [i]
            else:
                interval.append(i)
    ans = max(ans, interval[-1]-interval[0]+1)
    print(ans)