def counter(n, value, dist):
    if (value - dist) <= 0:
        return n-(dist-value)
    return value - dist

def clock(n, value, dist):
    if value + dist > n:
        return (value+dist)%n
    return value + dist


for _ in range(int(input())):
    n, m, x = map(int, input().split())
    
    vec = [[0]*(m+1) for i in range(n+1)]

    vec[x][0] = 1
    for move in range(1, m+1):
        dist, q = list(input().split())
        dist = int(dist)
        for value in range(1, n+1):
            if vec[value][move-1]:
                if q == "0":
                    new_val = clock(n, value, dist)
                    vec[new_val][move] = 1
                elif q == "1":
                    new_val = counter(n, value, dist)
                    vec[new_val][move] = 1
                else:
                    new_val = clock(n, value, dist)
                    vec[new_val][move] = 1
                    new_val_1 = counter(n, value, dist)

                    # print(f"val {value} clock {new_val} counter {new_val_1}")
                    vec[new_val_1][move] = 1

    ans = []
    for value in range(1, n+1):
        if vec[value][m]:
            ans.append(str(value))

    print(len(ans))
    print(" ".join(ans)) 