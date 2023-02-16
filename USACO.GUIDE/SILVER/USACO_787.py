input = open('rental.in', 'r').readline
fout = open('rental.out', 'w')



n, m, r = map(int, input().split())

cows = []
mqp = []
rent = []
for i in range(n):
    cows.append(int(input()))

for i in range(m):
    mqp.append(list(map(int, input().split())))

for i in range(r):
    rent.append(int(input()))

i = 0
j = 0

cows.sort(reverse=True)
mqp.sort(reverse=True, key=lambda x: [x[1], x[0]])
rent.sort(reverse=False)

cows_milked = [0]*n

while i < n and j < m:
    v = min(cows[i], mqp[j][0])
    cows_milked[i] += mqp[j][1]*v
    cows[i] -= v
    mqp[j][0] -= v
    if cows[i] == 0:
        i += 1
    if mqp[j][0] == 0:
        j += 1

i = 0
j = 0

# print(cows_milked)
# print(rent)

while n-1-i > -1 and r-1-j > -1:
    if rent[r-1-j] > cows_milked[n-1-i]:
        cows_milked[n-1-i] = rent[r-1-j]
        i += 1
        j += 1
    else:
        break
print(sum(cows_milked), file=fout)