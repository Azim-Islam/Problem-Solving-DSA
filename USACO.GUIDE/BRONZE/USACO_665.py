inputs = open('cowsignal.in', 'r')
print = lambda x : open('cowsignal.out', 'w').write(str(x))

M, N, K = map(int, inputs.readline().split())
ans = ""

for _ in range(int(M)):
    inp = inputs.readline().strip()
    for i in range(K):
        ans += "".join([i*K for i in inp])
        ans += '\n'

print(ans)