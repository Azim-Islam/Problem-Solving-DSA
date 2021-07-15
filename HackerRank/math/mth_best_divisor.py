def bestDivisors(d):
    return sum(map(int, str(d)))
divisors = []
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        divisors.append(i)
print(max(divisors, key=bestDivisors))