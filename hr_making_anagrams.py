from collections import Counter
s1 = Counter(input())
s2 = Counter(input())
uniqes = set(list(s1.keys())+ list(s2.keys()))
count = 0
for k in uniqes:
    count += abs(s1[k]-s2[k])
print(count)