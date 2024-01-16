
input = open("berries.in", "r").readline
fout = open("berries.out", "w")

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(1, max(arr) + 1):
    full = 0

    for j in arr:
        full += j // i

    if full >= k:
        ans = max(ans, k//2 * i)
    else: # We have extra empty baskets. 
        arr.sort(reverse=True, key=lambda x: x%i)
        v = max(full - k//2, 0)
        ans0 = v*i
        for j in range(0, min(k//2 - v, len(arr) - max(0, k//2-full))):
            ans0 += arr[j + max(0, k//2-full)]%i

        ans = max(ans, ans0)

print(ans, file=fout)