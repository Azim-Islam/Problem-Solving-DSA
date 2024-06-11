from collections import Counter


def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x


def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)


def distinct_factors(n):
    """returns a list of all distinct factors of n"""
    factors = [1]
    for p, exp in prime_factors(n).items():
        factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
    return factors


def all_factors(n):
    """returns a sorted list of all distinct factors of n"""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small


for _ in range(int(input())):
    arr = list(map(int, input().split()))
    volume = arr.pop()
    arr.sort()
    d = prime_factors(volume)
    d = [[k, d[k]] for k in d]
    d.sort(reverse=True)
    if volume == 1:
        print((arr[0]-1+1)*(arr[1]-1+1)*(arr[2]-1+1))
    elif len(d) > 3:
        print(0)
    else:
        t1 = 1
        t2 = 1
        t3 = 1

        while d and arr[0] >= t1*d[-1][0]:
            t1 *= d[-1][0]
            d[-1][1] -= 1
            if not d[-1][1]:
                d.pop()

        while d and arr[1] >= t2*d[-1][0]:
            t2 *= d[-1][0]
            d[-1][1] -= 1
            if not d[-1][1]:
                d.pop()
                
        while d and arr[0] >= t3*d[-1][0]:
            t3 *= d[-1][0]
            d[-1][1] -= 1
            if not d[-1][1]:
                d.pop()

        print((arr[0]-t1+1)*(arr[1]-t2+1)*(arr[2]-t3+1))


    # 2, 3, 5