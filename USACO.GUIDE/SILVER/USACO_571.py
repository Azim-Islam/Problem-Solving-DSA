input = open("highcard.in", 'r').readline
fout = open("highcard.out", 'w')

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

bess = list(set([i for i in range(1, n*2+1)]) - set(arr)) 
bess.sort()



c = 0

for _ in range(n):
    if arr[-1] < bess[-1]:
        arr.pop()
        bess.pop()
        c += 1
    else:
        arr.pop()

print(c, file=fout)