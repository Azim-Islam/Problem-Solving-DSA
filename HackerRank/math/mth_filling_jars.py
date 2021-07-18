n, m = map(int, input().split())
total = 0
for _ in range(m):
    a, b, k = map(int, input().split())
    total += (b-a+1)*k
    
print(int(total/n))