

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a = [0]*101
    for i in arr:
        a[i] += 1

    print(n-max(a))