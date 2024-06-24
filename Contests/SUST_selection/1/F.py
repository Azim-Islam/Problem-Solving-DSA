n = int(input())
from math import sqrt


d = n
for i in range(2, int(sqrt(n))+1):
    if n%i == 0:
        d = i
        break
print(1+(n-d)//2)