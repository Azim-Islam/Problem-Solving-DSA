from decimal import *
getcontext().prec = 800
t = int(input())
for _ in range(t):
    print(round(Decimal((input())).sqrt()))