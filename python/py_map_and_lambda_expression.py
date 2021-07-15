def nFib(n):
    n1 = 0
    n2 = 1
    numbers = []
    for i in range(n):
        numbers.append(n1)
        tmp = n2
        n2 = n1+n2
        n1 = tmp
    return numbers
n = int(input())

print(list(map(lambda x: x*x*x, nFib(n))))
