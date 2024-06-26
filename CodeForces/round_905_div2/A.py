from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = Counter(input())
    count = 0
    for c in s:
        if s[c]%2 and k:
            s[c] -= 1
            k -= 1
        elif s[c]%2:
            count += 1
    
    if count > 1:
        print("NO")
    else:
        print("YES")