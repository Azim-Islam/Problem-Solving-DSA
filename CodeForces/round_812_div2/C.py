def solve(n):
    i = n - 1
    arr = [0]*n
    mark = [0]*n
    while i > 0:
        v = (int((2*i)**0.5))**2
        while True:
            if abs(v-i) < n and not mark[abs(v-i)]:
                arr[i] = abs(v-i)
                mark[abs(v-i)] = 1
                i -= 1
            else:
                break
    print(*arr)


for _ in range(int(input())):
    n = int(input())
    solve(n)
