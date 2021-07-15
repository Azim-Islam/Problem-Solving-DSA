from math import sqrt
int = int
sqrt = sqrt


def isPrime(n):
    for j in range(2, int(sqrt(n))+1):
        if n % j == 0 and n != j:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    fact = 1
    count = 0
    for i in range(2, n+1):
        if isPrime(i):
            if fact*i > n:
                break
            else:
                fact = fact*i
                count += 1
    print(count)
