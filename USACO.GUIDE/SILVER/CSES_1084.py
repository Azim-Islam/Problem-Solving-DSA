n, m, k = map(int, input().split())
dsize = list(map(int, input().split()))
size = list(map(int, input().split()))


i = 0
j = 0

c = 0

dsize.sort()
size.sort()

while j < m and i < n:
    if dsize[i]-k <= size[j] <= dsize[i]+k:
        c += 1
        j += 1
        i += 1
    elif dsize[i]-k > size[j]:
        j += 1
    elif dsize[i]+k < size[j]:
        i += 1

print(c)