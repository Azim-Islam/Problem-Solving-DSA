from collections import defaultdict
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    upore = []
    niche = []
    niche_ase = [0]*(n + 2)
    upore_ase = [0]*(n + 2)

    for i in range(n):
        x, y = map(int, input().split())
        if y == 0:
            niche_ase[x] = 1
        else:
            upore_ase[x] = 1

    upore = sum(upore_ase)
    niche = sum(niche_ase)
    ans = 0
    c = 0
    for i in range(n+1):
        if upore_ase[i] and niche_ase[i]:
            ans += upore - 1 + niche - 1
        if upore_ase[i]:
            if i-1 >= 0 and niche_ase[i-1] and niche_ase[i+1]:
                # print("upore", i-1, i, i+1)
                c += 1
        if niche_ase[i]:
            if i-1 >= 0 and upore_ase[i-1] and upore_ase[i+1]:
                # print("niche", i-1, i, i+1)
                c += 1

    # print(upore_ase)
    # print(niche_ase)
    print(ans + c, file=sys.stdout)




        
    