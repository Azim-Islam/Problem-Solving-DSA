from random import randint
import sys

n = 10
m = 5
q = 3

print(n, m, q, file=sys.stdout)
for i in range(n):
    print(randint(1, 20), randint(1, m), file=sys.stdout)

arr = []
for i in range(m):
    arr.append(randint(0, 20))

print(*arr, file=sys.stdout)

for i in range(q):
    print(randint(0, 20), file=sys.stdout)