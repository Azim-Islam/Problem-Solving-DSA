from collections import defaultdict


def check(arr, c, i):
    if c[arr[i]] - 1 > 0:
        return True
    return False

def check_rev(arr, c, j):
    if c[arr[j]] - 1 > 0:
        return True
    return False

n = int(input())
arr = list(input())

count = defaultdict(int)

for c in arr:
    count[c] += 1
    
i = 0
j = n - 1
# print(count)
ans = []

while True:
    if check(arr, count, i):
        count[arr[i]] -= 1
        i += 1
    else:
        break
while True:
    if check_rev(arr, count, j):
        count[arr[j]] -= 1
        j -= 1
    else:
        break

ans.append(abs(i-j-1))
count = defaultdict(int)

for c in arr:
    count[c] += 1

i = 0
j = n - 1

while True:
    if check_rev(arr, count, j):
        count[arr[j]] -= 1
        j -= 1
    else:
        break

while True:
    if check(arr, count, i):
        count[arr[i]] -= 1
        i += 1
    else:
        break

ans.append(abs(i-j-1))

print(min(ans))
