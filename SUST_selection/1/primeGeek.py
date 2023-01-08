
import math as mt
 
MAXN = 10**7+1
 

spf = [0 for i in range(MAXN)]
 

def sieve():
    spf[1] = 1
    for i in range(2, MAXN):

        spf[i] = i

    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
         
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i

def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
 
    return ret
 

sieve()

from collections import Counter

def calc(l):
    c = Counter(l)
    a = 1
    for v in c.values():
        a *= (v+1)
    return a

x = int(input())
ans = 0
for i in range(1, x+1):
    ans += i * calc(getFactorization(i))
print(ans)