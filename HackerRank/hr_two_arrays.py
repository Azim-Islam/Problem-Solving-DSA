for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    for i, j in zip(a, b):
        if i + j < k:
            print("NO")
            break
    else:
        print("YES")
