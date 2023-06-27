# input = open('wormsort.in', 'r').readline
# fout = open('wormsort.out', 'w')

n, m = map(int, input().split())
tmp = [0] + list(map(int, input().split()))
arr = [0]*(n+1)

for i in range(1, n+1):
    arr[tmp[i]] = i

queries = []
for _ in range(m):
    q = list(map(int, input().split()))
    q[0], q[1] = min(q[0], q[1]), max(q[0], q[1])
    queries.append(q)

queries.sort(reverse=True, key = lambda x: x[2])

ans = float('inf')

while True:
    for q in queries:
        s, e, w = q[0], q[1], q[2]
        if arr[s] > arr[e]:
            ans = min(ans, w)
            arr[s], arr[e] = arr[e], arr[s]
            break
    else:
        print(arr)
        break

if ans == float('inf'):
    print("-1")
else:
    print(ans)