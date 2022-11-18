from collections import defaultdict

input = open('revegetate.in', 'r').readline
print = lambda x : open('revegetate.out', 'w').write(str(x)+'\n')

n, m = map(int, input().split())

c_arr = [0]*(n+1)
d = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

for i in range(1, n+1):
    s_c = set()
    a_c = {1,2,3,4}
    for v in d[i]:
        s_c.add(c_arr[v])
    c = a_c - s_c
    c_arr[i] = min(c)

print("".join([str(i) for i in c_arr[1:]]))


