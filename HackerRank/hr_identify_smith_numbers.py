
from math import sqrt


n = int(input())

def prime_numbers(n):
    primes = [2]
    for i in range(3, int(sqrt(n))+1):
        for j in primes:
            if i%j == 0:
                break
        else:
            primes.append(i)
    
    return primes

def prime_factors(n):
    primes = prime_numbers(n)
    i = 0
    factors = []
    while n > 0 and i < len(primes):
        if n%primes[i] == 0:
            n = n//primes[i]
            factors.append(primes[i])
        else:
            i += 1
    # print(factors)
    return factors

def digit_sum(n):
    dig = []
    while n > 0:
        dig.append(n%10)
        n = n//10
    return sum(dig)
    

s1 = 0
s2 = 0
factors = prime_factors(n)

if len(factors) < 1:
    print(0)
    exit(0)

tmp_n = n
for i in factors:
    if tmp_n%i == 0:
        tmp_n = tmp_n//i

if tmp_n > 0:
    factors_tmp = prime_factors(tmp_n)
    for i in factors_tmp:
        if tmp_n%i == 0:
            break
    else:
        if factors[-1] < tmp_n:
            factors.append(tmp_n)

for i in factors:
    s1 += digit_sum(i)

s2 += digit_sum(n)

if s1==s2:
    print(1)
else:
    print(0)