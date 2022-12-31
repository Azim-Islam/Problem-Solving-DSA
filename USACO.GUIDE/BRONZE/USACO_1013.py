input = open('swap.in', 'r').readline
fout = open('swap.out', 'w')

n, k = map(int, input().split())
l1, r1 = map(int, input().split())
l2, r2 = map(int, input().split())

def fk(i):
    if l1 <= i <= r1:
        i = l1 - i + r1
    if l2 <= i <= r2:
        i = l2 - i + r2
    return i

ans = [0]*(n+1)
for i in range(1, n+1):
    cp = fk(i)
    c = 1
    while cp != i:
        c += 1
        cp = fk(cp)
    L = k%c
    for _ in range(L):
        cp = fk(cp)
    ans[cp] = i

for i in range(1, n+1):
    print(ans[i], sep='\n', file=fout)

