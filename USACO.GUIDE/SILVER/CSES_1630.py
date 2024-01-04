import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


arr.sort(key=lambda x: x[0])

c = 0
ans = 0
for i, v in arr:
    ans += v - (i+c) 
    c = i + c
print(ans, file=sys.stdout)