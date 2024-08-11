from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))


d = defaultdict(int)

for i in range(0, n-1):
    d[i+2] = arr[i]

ans = [n]

node = n 


while node != 1:
    node = d[node]
    ans.append(node)

print(*ans[::-1])