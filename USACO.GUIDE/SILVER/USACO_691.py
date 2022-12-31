input = open('hps.in', 'r').readline
fout = open('hps.out', 'w')

from collections import defaultdict


def find_wins(i, d):
    m0 = 0
    for char in set(['P', 'H', 'S']):
        t1 = d[char][i] - d[char][0]
        m1 = 0
        for char0 in set(['P', 'H', 'S']) - set(char):
            m1 = max(m1, d[char0][-1] - d[char0][i])
        m0 = max(m0,  t1 + m1)
    return m0




def solve():
    n = int(input())
    arr = []

    for i in range(n):
        arr.append(input().strip())

    f = lambda : [0]
    d = defaultdict(f)

    for i, v in enumerate(arr):
        d[v].append(d[v][-1] + 1)
        for v0 in set(['P', 'H', 'S']) - set(v):
            d[v0].append(d[v0][-1])
    m = 0
    for i in range(n+1):
        m = max(m, find_wins(i, d))

    print(m, file=fout)