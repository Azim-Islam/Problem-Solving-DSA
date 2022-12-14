input = open('maxcross.in', 'r').readline
fout = open('maxcross.out', 'w')

n, k, b = map(int, input().split())

s = set()
for i in range(b):
    s.add(int(input()))

cum_sum = [0]
for i in range(1, n+1):
    if i in s:
        cum_sum.append(cum_sum[-1] + 1)
    else:
        cum_sum.append(cum_sum[-1])

# Sliding window
ans = float('inf')
for i in range(1, n+1 - k+1):
    ans = min(ans, cum_sum[i+k-1] - cum_sum[i-1])
print(ans, file=fout)