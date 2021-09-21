#https://www.hackerrank.com/challenges/greedy-florist/problem

#Max Score - 35


n, m = map(int, input().split())
c = list(map(int, input().split()))

manush = [1]*m
c.sort(reverse=True)


k = 0
total_sum = 0

for i in c:
    total_sum += manush[k]*i
    manush[k] += 1
    
    if k+1 > m - 1:
        k = 0
    else:
        k += 1
        
print(total_sum)
    