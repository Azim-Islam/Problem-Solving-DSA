#https://www.hackerrank.com/challenges/beautiful-pairs/
#points 30

from collections import Counter, defaultdict


    
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_counter = Counter(A)
B_counter = Counter(B)

ans = 0
for i in A_counter.keys():
    if i in B_counter:
        ans += min(A_counter[i], B_counter[i])

if ans == n:
    print(ans-1)
else:
    print(ans+1)
    