from collections import defaultdict

input = open('div7.in', 'r').readline
fout = open('div7.out', 'w')

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


d = defaultdict(list)

cum = 0
max_len = 0
for i, v in enumerate(arr):
    cum = (v + cum)%7
    d[cum].append(i)
    max_len = max(max_len, d[cum][-1] - d[cum][0])

print(max_len, file=fout)