n, l = map(int, input().split())
arr = list((list(map(int, input().split()))))

arr.sort()

min_dist = max((arr[0] - 0), l - arr[-1])
for i in range(0, n-1):
    min_dist = max(min_dist, (arr[i+1]-arr[i])/2)


print(min_dist)