n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

rad = 0
for i in range(n-1):
    rad = max(rad, (arr[i+1] - arr[i])/2)

rad = max(rad, (l-arr[-1]))
rad = max(rad, (arr[0]-0))
print(rad)