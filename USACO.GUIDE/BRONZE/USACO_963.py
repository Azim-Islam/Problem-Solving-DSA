from collections import defaultdict
inputs = open('gymnastics.in', 'r')
# print = lambda x : open('gymnastics.out', 'w').write(str(x)+'\n')

k, n = map(int, inputs.readline().split())
arr = []
for _ in range(k):
    arr.append(list(map(int, inputs.readline().split())))

dlist = lambda : [99999, -1]
cow_pos = defaultdict(dlist)

for i in arr:
    for j in range(len(i)):
        #(min, max) position of the Nth cow!
        cow_pos[i[j]][0] = min(j, cow_pos[i[j]][0])
        cow_pos[i[j]][1] = max(j, cow_pos[i[j]][1])
n -= 1
max_ = n*(n+1)//2

minus = 0
for i in cow_pos.values():
    minus += abs(i[0]-i[1])
    
minus = minus//2


print(max_-minus)