from bisect import bisect_right

input = open('lifeguards.in', 'r').readline
fout = open('lifeguards.out', 'w')

n = int(input())
arr = []
comp = set()

def compIdx(arr, i):
    return bisect_right(arr, i) - 1


for i in range(n):
    s, e = map(int, input().split())
    comp.add(s)
    comp.add(e)
    arr.append([s, e])

comp = sorted(comp)
diff_arr = [0]*len(comp)

for s, e in arr:
    diff_arr[compIdx(comp, s)] += 1
    diff_arr[compIdx(comp, e)] -= 1

for i in range(1, len(diff_arr)):
    diff_arr[i] = diff_arr[i] + diff_arr[i-1]

prefix = [0]*(len(diff_arr))
width = [0]*(len(diff_arr))

for i in range(len(diff_arr) - 1):
    width[i] = comp[i+1] - comp[i]
width[-1] = width[-2]
    
zeros = 0
if diff_arr[0] == 1:
    prefix[0] = width[0] * 1
elif diff_arr[0] == 0:
    zeros = width[0] 

for i in range(1, len(diff_arr)):
    if diff_arr[i] == 1:
        prefix[i] = width[i] + prefix[i-1]
    else:
        prefix[i] = prefix[i-1]
    if diff_arr[i] == 0:
        zeros += width[i]

prefix = [0]+prefix
ans = comp[-1]
#need to minus the 0s
x0 = float('inf')
for s, e in arr:
    s0 = compIdx(comp, s) + 1
    e0 = compIdx(comp, e) + 1
    x0 = min(x0, prefix[e0-1]-prefix[s0-1])

# print(diff_arr)
# print(prefix)
print(ans - x0 - zeros, file=fout)