from collections import defaultdict


input = open('notlast.in', 'r').readline
print = lambda x : open('notlast.out', 'w').write(str(x)+'\n')
# input = open('in', 'r').readline


d = defaultdict(int)
d = {k:0 for k in "Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, Henrietta".split(", ")}

n = int(input())
for _ in range(n):
    k, v = input().split()
    d[k] += int(v)

v = sorted(set(d.values()))[1]
ans = []
for k in d:
    if d[k] == v:
        ans.append(k)

if len(ans) > 1:
    print("Tie")
else:
    print(ans[-1])