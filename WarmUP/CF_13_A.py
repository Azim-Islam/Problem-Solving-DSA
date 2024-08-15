from fractions import Fraction
import fractions


def digis_base(n, b):
    s = 0
    while n >= b:
        s += n % b
        n = n//b
    s += n
    return s
def find_dig(n):
    sum = 0
    for i in range(2, n):
        sum += digis_base(n, i)
    return sum

n = int(input())
