def fibonacci(n1, n2, n):

    next = n1
    while n > 1:
        next = n1 + n2**2
        n1 = n2
        n2 = next
        n -= 1
    return n1

t1 , t2, n = map(int, input().split())
print(fibonacci(t1, t2, n))