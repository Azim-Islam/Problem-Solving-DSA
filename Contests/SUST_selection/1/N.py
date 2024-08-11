n = int(input())
from math import sqrt
from collections import Counter

# first find primes


def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res

primes = prime_list(10**7)


dp = dict()
def merge(c, dp):
    for k in dp:
        c[k] += dp[k]
    return c

def find(i):
    t = i
    c = Counter()
    a = 1
    for p in primes:
        if i in dp:
            a = dp[i]
            for v in c.values():
                a *= (v+1)
            dp[t] = a
            return a
        while i % p == 0:
            c[p] += 1
            i //= p
        if 
    
    for v in c.values():
        a *= (v+1)
    dp[t] = a
    return a


ans = 0
for i in range(1, n+1):
    ans += i*find(i)

print(ans)