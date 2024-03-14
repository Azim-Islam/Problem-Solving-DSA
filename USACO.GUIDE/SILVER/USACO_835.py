input = open("lemonade.in", 'r').readline
fout = open("lemonade.out", 'w')

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

c = 0

for i, w in enumerate(arr):
    if i > w:
        break
    c += 1

print(c, file=fout)
