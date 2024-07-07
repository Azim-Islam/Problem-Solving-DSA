n, k = map(int, input().split())
arr = list(map(int, input().split()))

ones = [0]*(k+1)
twos = [0]*(k+1)
ans = 0

for i in range(0, n, k):
    sub_arr = arr[i:i+k]
    for j in range(k):
        if sub_arr[j] == 1:
            ones[j] += 1
        else: twos[j] += 1

ans = 0
for i in range(k):
    ans += min(n//k - ones[i], n//k - twos[i])

print(ans)