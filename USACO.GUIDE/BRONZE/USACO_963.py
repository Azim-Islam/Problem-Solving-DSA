read = open('gymnastics.in', 'r').readline
write = lambda x : open('gymnastics.out', 'w').write(str(x))

def solve():
    k, n = map(int, read().split())
    arr = []
    rev_arr = []
    for i in range(k):
        arr.append(list(map(int, read().split())))
        rev_arr.append([0]*(n+1))
        for i in range(n):
            rev_arr[-1][arr[-1][i]] = i  
    count = 0
    for i in range(n):
        v = arr[0][i]
        for j in range(i+1, n):
            u = arr[0][j]
            bool_c = True
            for c in range(1, k):
                v0, u0 = rev_arr[c][v], rev_arr[c][u]
                if v0 > u0:
                    break
            else:
                count +=1
    write(count)

solve()