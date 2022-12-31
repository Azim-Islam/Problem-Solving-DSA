
from collections import defaultdict
import sys

print = lambda x : open('citystate.out', 'w').write(str(x)+'\n')
input = open('citystate.in', 'r').readline
# input = open('in', 'r').readline
 

n = int(input())
d = defaultdict(lambda: defaultdict(int))

for i in range(n):
    c, s = input().split()
    c = c.lower()
    s = s.lower()
    d[s][c[:2]] += 1

count = 0
count1 = 0
# print(d)
ans = ""
bl = set()
for k in d:
    bl.add(k)
    for k1 in d[k]:
        if k1 not in bl:
            c1 = 0 
            c2 = 0
            if k1 in d:
                c1 = d[k1][k]
            if k in d:
                c2 = d[k][k1]
            if k1 == k:
                count1 += ((c1-1)*(c1-2))//2
            else:
                count += c1*c2
            
print(count+count1)