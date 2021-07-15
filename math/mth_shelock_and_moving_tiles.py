from math import sqrt

a, s1, s2 = map(int, input().split())

def swap(p1, p2):
    if p1>=p2:
        return p1, p2
    else:
        return p2, p1
    
for _ in range(int(input())):
    area = int(input())
    v1, v2 = swap(s1,s2)
    t = (sqrt(area)-a)*sqrt(2)/(v2-v1)
    print(abs(t))