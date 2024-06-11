def BS(container, v):
    lo = 0
    hi = len(container)
    while lo < hi:
        mid = (lo + hi)//2
        if container[mid][-1] <= v:
            hi = mid
        else:
            lo = mid + 1
    return hi


def insert(container, v):
    idx = BS(container, v)
    if idx == len(container):
        container.append([v])
    else:
        container[idx].append(v)



n = int(input())
arr = list(map(int, input().split()))
container = []

for i in arr:
    insert(container, i)


for a in container:
    print(*a)