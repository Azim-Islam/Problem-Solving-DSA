n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
s = 0
for i in range(n+1):
    if sum(arr[:i]) > x:
        print(i-1)
        break
else:
    print(i)