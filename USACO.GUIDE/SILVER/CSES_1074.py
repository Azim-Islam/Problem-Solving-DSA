n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = arr[n//2]

c = 0

for i in arr:
    c += abs(i-m)

print(c)