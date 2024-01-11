input = open("reststops.in", 'r').readline
fout = open("reststops.out", 'w')


class P:
    def __init__(self, x, c):
        self.x = x
        self.c = c

L, N, rf, rb = map(int, input().split())

arr = []

for _ in range(N):
    x, c = map(int, input().split())
    arr.append(P(x, c))

prev = P(arr[-1].x, arr[-1].c)
ans = 0

for i in range(N-1, -1, -1):
    if arr[i].c > prev.c:
        l = prev.x - arr[i].x
        s = rf*l - rb*l
        ans += prev.c * s
        prev = arr[i]

l = prev.x
s = rf*l - rb*l
ans += prev.c * s

print(ans, file=fout)