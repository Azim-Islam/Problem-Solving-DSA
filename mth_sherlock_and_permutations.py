def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    m -= 1
    print(abs(fact(n+m)//((fact(n)*fact(m))))%(10**9+7))