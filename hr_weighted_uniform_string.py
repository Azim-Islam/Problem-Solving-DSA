from collections import defaultdict
from itertools import groupby
d = defaultdict(int)
string = input()

for k, v in groupby(string):
    val = ord(k)-96
    weight = val*(len(list(v)))
    if weight > d[val]:
        d[val] = weight

for _ in range(int(input())):
    n = int(input())
    for k, v in d.items():
        if n%k == 0 and v >= n:
            #print(k, v, n)
            print("Yes")
            break
    else:
        print("No")