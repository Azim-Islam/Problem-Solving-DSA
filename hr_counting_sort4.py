n = int(input())
array =  [[] for _ in range(100)]
for k in range(n):
    i, s = input().split()
    i = int(i)
    if k < n/2:
        array[i].append('-')
    else:
        array[i].append(s)
for i in array:
    if i:
        print(' '.join(i), end=' ')