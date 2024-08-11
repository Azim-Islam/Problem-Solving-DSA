from math import ceil


n, m, a, b = map(int, input().split())

ans = min((n%m)*b, ((ceil(n/m)*m - n)*a))
print(ans) 