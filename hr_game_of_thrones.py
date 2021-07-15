from collections import Counter
strc = Counter(input())
odd = 0
for values in strc.values():
    if values%2 == 1:
        odd += 1
if odd > 1:
    print("NO")
else:
    print("YES")
#print(strc)