from collections import defaultdict
from itertools import permutations

input = open('lineup.in', 'r').readline
fout = open('lineup.out', 'w')

n = int(input())
d = defaultdict(list)

    

def check_valid(order: list, d):
    for u in d:
        i = order.index(u)
        for v in d[u]:
            if not (v == order[min(7, i+1)] or v == order[max(0, i-1)]):
                return False
    return True
        



for i in range(n):
    line = input().strip()
    d[line[0]].append(line[-1])
    d[line[-1]].append(line[0])


cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
cows.sort()
order_permutations = permutations(cows)

for order in order_permutations:
    if check_valid(order, d):
        print(*order, sep="\n", file=fout)
        break   