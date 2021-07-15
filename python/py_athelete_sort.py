n, m = map(int, input().split())
data = []
for i in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)
k = int(input())
data.sort(key=lambda x: x[k])
[print(*i) for i in data]