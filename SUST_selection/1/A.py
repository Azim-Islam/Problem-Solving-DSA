from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
c = Counter(arr)

ans = c[4]
ans += c[3]
c[1] -= min(c[1], c[3])
ans += c[2]//2
ans += c[2]%2
c[1] -= min(c[1], c[2]%2*2)
ans += c[1]//4
ans += 1 if c[1]%4 else 0


print(ans)