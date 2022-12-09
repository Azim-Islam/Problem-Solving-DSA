from collections import defaultdict

input = open('evolution.in', 'r').readline
fout = open('evolution.out', 'w')

n = int(input())

sets = defaultdict(set)

for i in range(n):
    k, *characteristic = input().split()
    sets[i] = set(characteristic)

def solve(sets):
    for i in sets:
        set_a = sets[i]
        for j in range(i+1, n):
            set_b = sets[j]
            if not (set_a.issuperset(set_b) or set_b.issuperset(set_a)):
                for k in range(n):
                    set_c = sets[k]
                    if set_c.issuperset(set_a) and set_c.issuperset(set_b):
                        return False
    return True

if solve(sets):
    print("yes", file=fout)
else:
    print("no", file=fout)