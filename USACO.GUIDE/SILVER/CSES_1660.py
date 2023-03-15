import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

pref_sum = [0]

for i in arr:
    pref_sum.append(pref_sum[-1]+i)

i = 0
j = 0
count = 0
while not(i==n and j == n):
    if pref_sum[j] - pref_sum[i] == x:
        count += 1
        i = min(i+1, n)
    elif pref_sum[j] - pref_sum[i] > x:
        i = min(i+1, n)
    elif pref_sum[j] - pref_sum[i] < x:
        j = min(j+1, n)
        if j == n and pref_sum[j] - pref_sum[i] < x:
            break

print(count)
    