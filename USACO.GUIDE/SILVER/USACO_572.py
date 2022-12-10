input = open('bcount.in', 'r').readline
fout = open('bcount.out', 'w')

def solve():
    n, q = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))


    cum_1 = [0]
    cum_2 = [0]
    cum_3 = [0]

    for i in arr:
        if i == 1:
            cum_1.append(cum_1[-1] + 1)
            cum_2.append(cum_2[-1])
            cum_3.append(cum_3[-1])
        if i == 2:
            cum_2.append(cum_2[-1] + 1)
            cum_1.append(cum_1[-1])
            cum_3.append(cum_3[-1])
        if i == 3:
            cum_3.append(cum_3[-1] + 1)
            cum_2.append(cum_2[-1])
            cum_1.append(cum_1[-1])

    res = []
    for i in range(q):
        l, r = map(int, input().split())
        a1 = cum_1[r] - cum_1[l-1]
        a2 = cum_2[r] - cum_2[l-1]
        a3 = cum_3[r] - cum_3[l-1]
        res.append(f"{a1} {a2} {a3}")
    print("\n".join(map(str, res)))
    
solve()