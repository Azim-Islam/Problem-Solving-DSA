n = int(input())
arr = list(map(int, input().split()))


count = 0 
for i in range(n):
    sum_ = 0
    for j in range(i, n):
        sum_ += arr[j]
        avg = sum_/(j-i+1)
        for k in range(i, j+1):
            if arr[k] == avg:
                count += 1
                break

print(count)