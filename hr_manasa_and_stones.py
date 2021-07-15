for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    i = n-1
    j = 0
    result = []
    if n == 1:
        print(sorted([a,b]))
        continue
    while i>=0:
        perm = a*i + b*j
        i -= 1
        j += 1
        result.append(perm)
    print(*sorted(set(result)))