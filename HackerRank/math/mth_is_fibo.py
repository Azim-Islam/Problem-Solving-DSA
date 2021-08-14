from sys import stdin
from math import sqrt


def checkPerfectSquare(n):
    ans = sqrt(n)
    if ans == int(ans):
        return True
    else:
        return False
    
def isFibo(n):
    if checkPerfectSquare(5*pow(n, 2) + 4):
        print("IsFibo")
    elif checkPerfectSquare(5*pow(n, 2) - 4):
        print("IsFibo")
    else:
        print("IsNotFibo")
    
for _ in range(int(input())):
    n = int(stdin.readline())
    isFibo(n)