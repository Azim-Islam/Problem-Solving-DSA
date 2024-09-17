from collections import Counter

n = int(input())
arr = list(input())

c = Counter(arr)
l = 0
o = 0
ans = 0
for i, v in enumerate(arr):
    if v == "L":
        l += 1
        c["L"] -= 1
    else:
        o += 1
        c["O"] -= 1

    if c["L"] != l and c["O"] != o:
        ans = i
        break

if ans == n-1:
    print("-1")
else:
    print(ans+1)