from collections import Counter


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    c = Counter(arr)
    for k in c:
        count += c[k]//3
    print(count)