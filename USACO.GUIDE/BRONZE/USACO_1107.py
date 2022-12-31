from collections import defaultdict


n = int(input())

dx = ["ox", "tiger", "rabbit", "dragon", "snake", "horse", "goat", "monkey", "rooster", "dog", "pig", "rat"]
d = {dx[v]:v+1 for v in range(len(dx))}
d0 = defaultdict(int)
d0['bessie'] = 1

dd = defaultdict(int)
dd['bessie'] = 0


def calc(y1, y2, pon):

    if pon == "next":
        if y1 < y2:
            return y2 - y1
        else:
            return 12 - y1 + y2
    else:
        if y1 > y2:
            return y2 - y1
        else:
            return - y1 - (12 - y2)

for i in range(n):
    lines = input().lower().split()
    c1 = lines[0]
    pon = lines[3]
    year2 = lines[4]
    c2 = lines[-1]
    #find difference
    year1 = d0[c2]
    d0[c1] = d[year2]
    year2 = d[year2]
    diff = calc(year1, year2, pon)
    #save difference respective to c2
    dd[c1] = diff + dd[c2]

print(abs(dd['elsie']))
# print(dd)