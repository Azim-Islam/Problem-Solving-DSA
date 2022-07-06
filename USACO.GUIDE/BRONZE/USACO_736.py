read = open('cownomics.in', 'r').readline
write = lambda x : open('cownomics.out', 'w').write(str(x))

    # read = input
    # write = print
def solve():
    n, m = map(int, read().split())
    arr_s = [set() for i in range(m)]
    arr_p = [set() for i in range(m)]

    for i in range(n):
        a = list(read())
        [arr_s[j].add(a[j]) for j in range(m)]

    for j in range(n):
        a = list(read())
        [arr_p[j].add(a[j]) for j in range(m)]

    count = 0
    for i in range(m):
        if len(arr_s[i].intersection(arr_p[i])) == 0:
            count += 1
    write(count)
solve()