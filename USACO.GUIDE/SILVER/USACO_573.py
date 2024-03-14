input = open("cardgame.in", 'r').readline
fout = open("cardgame.out", 'w')


n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

bess = list(set([i for i in range(1, n*2+1)]) - set(arr)) 
bess.sort(reverse=True)

f_arr = arr[:n//2]
l_arr = arr[n//2:]

f_arr.sort()
l_arr.sort(reverse=True)

f_bess = bess[:n//2]
l_bess = bess[n//2:]

f_bess.sort()
l_bess.sort(reverse=True)


c = 0


for _ in range(n//2):
    if f_arr[-1] < f_bess[-1]:
        f_arr.pop()
        f_bess.pop()
        c += 1
    else:
        f_arr.pop()

for _ in range(n//2):
    if l_bess[-1] < l_arr[-1]:
        l_bess.pop()
        l_arr.pop()
        c += 1
    else:
        l_arr.pop()

print(c, file=fout)



