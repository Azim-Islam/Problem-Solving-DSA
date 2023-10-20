
input = open('diamond.in', 'r').readline
fout = open('diamond.out', 'w')



n, k = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(int(input()))

arr.sort()
ith_len = [0]*n
r_max = [0]*n
j = 0
for i in range(n):
    while j < n:
        if arr[j] - arr[i] <= k:
            j += 1
        else:
            break 
    ith_len[i] = j-i

r_max[-1] = 1
for i in range(n-2, -1, -1):
    r_max[i] = max(r_max[i+1], ith_len[i])
r_max.append(0)

ans = 0
for i in range(n):
    r_idx = i + ith_len[i]
    ans = max(ans, ith_len[i]+r_max[r_idx])


# print(arr)
# print(ith_len)
# print(r_max)
print(ans, file=fout)