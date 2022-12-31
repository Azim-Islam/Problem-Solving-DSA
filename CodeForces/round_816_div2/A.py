import sys
 
input = sys.stdin.readline

for _ in range(int(input())):
    r, c = map(int, input().split())
    meg = r-1+c-1
    stan = min([1+c-1, 1+r-1, r-1+c-1])
    cost = meg + stan
    print(cost)