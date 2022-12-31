

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    b = list(sorted(arr[:k], reverse=True))
    c = list(sorted(arr[k:]))
    # print(arr)
    # print(b, c)
    count = 0
    for i, v in zip(b, c):
        if i > v:
            count += 1
        else:
            break
    print(count)