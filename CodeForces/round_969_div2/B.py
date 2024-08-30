for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    ms = max(arr)
    max_values = []
    for i in range(m):
        q = list(input().split())

        if int(q[1]) <= ms <= int(q[2]):
            if q[0] == "+":
                ms += 1
            else:
                ms -= 1
        max_values.append(ms)

        
    print(*max_values)