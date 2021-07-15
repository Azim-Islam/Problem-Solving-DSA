from math import sqrt
from collections import defaultdict
import sys
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = primes(int(sqrt(1000000001)+1))
prime_count = defaultdict(int)

for _ in range(int(input())):
    prime_count = defaultdict(int)
    td = 1
    flag = 0
    n = int(sys.stdin.readline())
    if n%2 == 0:
        uniques = 1
        for i in primes:
            while n//i == n/i:
                n = n/i
                prime_count[i] += 1
        if n > 1:
            uniques += 1
            flag += 2

        for i in prime_count.keys():
            if i != 2:
                td = td*(prime_count[i]+1) 
                
        if flag:
            td = td*flag
            
        td = prime_count[2]*td

        print(td)

    else:
        print(0)
