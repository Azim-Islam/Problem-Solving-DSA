

inputs = open('blist.in', 'r')
print = lambda x : open('blist.out', 'w').write(str(x)+'\n')

N = int(inputs.readline())
cows = []
for _ in range(N):
    s, t, b = map(int, inputs.readline().split())
    cows.append((s, t, b))

# cows.sort(lambda x: x[0])
available_buckets = 0
total_buckets = N

for s, t, b in cows:
    available_buckets = 0
    taken = 0
    for s1, t1, b1 in cows:
        if s > s1 and s < t1:
            taken += b1
    available = N - taken
    if b > available:
        extras = b - available
        N += extras
print(N)